/**
 * Typesense Search Integration for Better Conversations Foundation Documentation
 * This replaces the default Sphinx search with Typesense-powered search
 */

(function() {
    'use strict';
    
    // Check if Typesense is loaded
    if (typeof Typesense === 'undefined') {
        console.error('Typesense library not loaded');
        return;
    }

    // Initialize Typesense client
    const typesenseClient = new Typesense.Client({
        nodes: [{
            host: 'typesense.bettercourses.org',
            port: 443,
            protocol: 'https'
        }],
        apiKey: '3dc57ebb7c46e57a5de5fa01d7c32c69855b3a04d26eaf5b5afff012d05641a4',
        connectionTimeoutSeconds: 2
    });

    // Search configuration
    const SEARCH_CONFIG = {
        collection: 'bcf-content',
        queryBy: 'title,content,excerpt',
        queryByWeights: '3,1,2',
        // Remove filter to show all content from the collection
        // filterBy: 'type:=documentation', 
        perPage: 20,
        highlightFullFields: 'title,content',
        highlightStartTag: '<mark>',
        highlightEndTag: '</mark>',
        snippetThreshold: 30
    };

    // Debounce function for search input
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    // Format search results
    function formatSearchResult(hit) {
        const doc = hit.document;
        const highlights = hit.highlights || [];
        
        // Get highlighted title or fallback to document title
        let title = doc.title;
        const titleHighlight = highlights.find(h => h.field === 'title');
        if (titleHighlight && titleHighlight.snippet) {
            title = titleHighlight.snippet;
        }
        
        // Get content snippet
        let snippet = doc.excerpt || '';
        const contentHighlight = highlights.find(h => h.field === 'content');
        if (contentHighlight && contentHighlight.snippet) {
            snippet = contentHighlight.snippet;
        }
        
        // Determine the correct URL
        let url = doc.slug;
        // Check if this is a documentation page (from this site)
        if (doc.type === 'documentation' || doc.id && doc.id.startsWith('docs-')) {
            // Use relative URL for documentation pages
            url = doc.slug;
        } else {
            // For main site content, redirect to localhost:4321 (dev environment)
            // In production, this should be the main site URL
            if (doc.slug && !doc.slug.startsWith('http')) {
                url = 'http://localhost:4321' + doc.slug;
            }
        }
        
        // Build result HTML
        return `
            <div class="search-result-item">
                <h4 class="search-result-title">
                    <a href="${url}">${title}</a>
                </h4>
                <p class="search-result-snippet">${snippet}</p>
                <div class="search-result-meta">
                    <span class="search-result-type">${doc.type}</span>
                    ${doc.tags && doc.tags.length > 0 ? 
                        `<span class="search-result-tags">${doc.tags.slice(0, 3).join(', ')}</span>` : ''
                    }
                </div>
            </div>
        `;
    }

    // Perform search
    async function performSearch(query) {
        if (!query || query.trim().length < 2) {
            return { hits: [], found: 0 };
        }

        try {
            const searchParameters = {
                q: query,
                query_by: SEARCH_CONFIG.queryBy,
                query_by_weights: SEARCH_CONFIG.queryByWeights,
                per_page: SEARCH_CONFIG.perPage,
                highlight_full_fields: SEARCH_CONFIG.highlightFullFields,
                highlight_start_tag: SEARCH_CONFIG.highlightStartTag,
                highlight_end_tag: SEARCH_CONFIG.highlightEndTag,
                snippet_threshold: SEARCH_CONFIG.snippetThreshold,
                sort_by: '_text_match:desc,date_timestamp:desc'
            };
            
            // Only add filter if it exists
            if (SEARCH_CONFIG.filterBy) {
                searchParameters.filter_by = SEARCH_CONFIG.filterBy;
            }

            const searchResult = await typesenseClient
                .collections(SEARCH_CONFIG.collection)
                .documents()
                .search(searchParameters);

            return searchResult;
        } catch (error) {
            console.error('Typesense search error:', error);
            return { hits: [], found: 0 };
        }
    }

    // Display search results
    function displayResults(results, container) {
        if (!results.hits || results.hits.length === 0) {
            container.innerHTML = '<div class="no-results">No results found</div>';
            return;
        }

        const resultsHTML = results.hits.map(hit => formatSearchResult(hit)).join('');
        container.innerHTML = `
            <div class="search-results-header">
                Found ${results.found} result${results.found !== 1 ? 's' : ''}
            </div>
            <div class="search-results-list">
                ${resultsHTML}
            </div>
        `;
    }

    // Initialize search when DOM is ready
    function initializeSearch() {
        // Find the search dialog
        const searchDialog = document.getElementById('pst-search-dialog');
        if (!searchDialog) {
            console.log('PyData search dialog not found, trying fallback');
            return;
        }

        let searchInitialized = false;
        let searchInput = null;
        let resultsContainer = null;

        // Function to setup the Typesense search UI
        function setupTypesenseSearch() {
            if (searchInitialized) return;
            
            // Create custom search container
            const customSearchContainer = document.createElement('div');
            customSearchContainer.id = 'typesense-search-container';
            customSearchContainer.innerHTML = `
                <div class="typesense-search-wrapper">
                    <input type="text" 
                           id="typesense-search-input" 
                           class="typesense-search-input" 
                           placeholder="Search documentation..."
                           autocomplete="off">
                    <div id="typesense-search-results" class="typesense-search-results"></div>
                </div>
            `;

            // Replace dialog content
            searchDialog.innerHTML = '';
            searchDialog.appendChild(customSearchContainer);

            // Get elements
            searchInput = document.getElementById('typesense-search-input');
            resultsContainer = document.getElementById('typesense-search-results');

            // Setup search handler
            const handleSearch = debounce(async (event) => {
                const query = event.target.value;
                
                if (query.length < 2) {
                    resultsContainer.innerHTML = '';
                    return;
                }

                resultsContainer.innerHTML = '<div class="searching">Searching...</div>';
                const results = await performSearch(query);
                displayResults(results, resultsContainer);
            }, 300);

            searchInput.addEventListener('input', handleSearch);
            searchInitialized = true;
        }

        // Hook into the existing PyData theme search functionality
        // Find all search buttons
        const searchButtons = document.querySelectorAll('.search-button, .search-button-field, .search-button__button');
        
        searchButtons.forEach(button => {
            // Remove existing click handlers by cloning
            const newButton = button.cloneNode(true);
            button.parentNode.replaceChild(newButton, button);
            
            // Add our handler
            newButton.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                
                if (!searchInitialized) {
                    setupTypesenseSearch();
                }
                
                if (searchDialog.open) {
                    searchDialog.close();
                } else {
                    searchDialog.showModal();
                    if (searchInput) {
                        searchInput.focus();
                    }
                }
            });
        });

        // Handle Cmd/Ctrl+K shortcut
        document.addEventListener('keydown', (e) => {
            if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
                e.preventDefault();
                
                if (!searchInitialized) {
                    setupTypesenseSearch();
                }
                
                if (searchDialog.open) {
                    searchDialog.close();
                } else {
                    searchDialog.showModal();
                    if (searchInput) {
                        searchInput.focus();
                    }
                }
            }
        });

        // Close on Escape (dialog handles this natively)
    }

    // Wait for DOM to be ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeSearch);
    } else {
        initializeSearch();
    }
})();