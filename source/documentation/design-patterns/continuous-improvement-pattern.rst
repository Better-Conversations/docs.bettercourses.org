.. _continuous-improvement-pattern:

===========================
Continuous Improvement (CI)
===========================

.. tags:: continuous-improvement, feedback, data, iterative, enhancement, documentation, quality-assurance, process, design, PDCA

-----------------------------------------------------------
:material-outlined:`construction;1.8rem` Using this pattern
-----------------------------------------------------------

This pattern describes the continuous improvement process for systematic refinement of course design and delivery methods. It is based on the PDCA cycle (Plan, Do, Check, Act). PDCA is a framework for continuous improvement that is used in many industries, including manufacturing, software development, and project management. It is a core part of our approach to Better Conversations.

The PDCA cycle is applied at a course level and at the session level. This allows us to quickly iterate on the course design and delivery methods to improve the learning experience for participants. The course level PDCA cycle is used to plan and review the overall course design, delivery and direction. The session level PDCA cycle is used to plan and review the design and delivery of each session.

.. todo::

   TODO incorporate intentions into the course overview and flight plan

   Learning intentions, rather than fixed objectives, guide our improvement process. These intentions focus on the purpose and direction of learning rather than rigid outcomes. For experiential learning like our Better Conversations courses, learning intentions provide a more appropriate framework than traditional learning objectives. They acknowledge the subjective nature of developing communication skills, create space for personal discovery, and accommodate the diverse starting points of our participants. This approach aligns perfectly with our qualitative observation process.

The overall process connects design and delivery patterns and improvements through structured observation and feedback. It covers how design changes feed into delivery and how delivery insights inform design.

------------------------------------------------   
:material-outlined:`design_services;1.8rem` Form
------------------------------------------------

Module-level improvements
-------------------------

This process mainly uses the latest :ref:`course-materials` and :ref:`delivery-patterns` to deliver the sessions and collect observations.

.. todo::

   TODO: Improve module level PDCA cycle

   .. graphviz::
      :align: center
      :alt: Module level PDCA Cycle
      :caption: Module level PDCA Cycle
      :layout: dot

      digraph PDCA {
         rankdir=TB;
         compound=true;
         splines=true;
         node [shape=box, style="rounded,filled", fontname="Arial"];
         edge [fontname="Arial"];
      
         A [label="Brief the session", fillcolor="white"];
         B [label="Deliver the session & collect observations", fillcolor="white"];
         C [label="Debrief the session", fillcolor="white"];
         D [label="Improve the next session", fillcolor="white"];

         A -> B -> C -> D;
         D -> A [constraint=false];
      }
      }

**Brief the session (Plan)** where the delivery team meets to prepare for and plan any small changes to the session, including discussing the flight plan, agreeing roles and performing equipment checks. During this briefing, the team reviews the learning intentions for the session to create shared understanding of purpose rather than just deliverables. Changes may include running small-scale experiments to test the impact of flight plan updates. We agree the changes between the delivery team and document them as observations.

**Deliver the session and collect observations (Do)** where the module content is delivered and more observations are collected. Observers focus on participant engagement, moments of insight, and challenges in relation to the learning intentions. We also capture feedback from participants if it is offered, paying special attention to their subjective experience and personal discoveries.

**Debrief the session (Check)** where the delivery team reviews the session, including sharing observations about what went well and what could be improved. These are added to the observations list. The team considers the quality of the learning experience rather than just task completion, looking for patterns in participant engagement and moments that either enhanced or hindered deeper learning.

**Improve the next session (Act)** where any immediate or urgent changes are made that need to be addressed before the next session. This might include adjustments to activities, timing, facilitation approaches, or producer support based on the observed participant experience and team reflection.

Course-level improvements
-------------------------

This stage improves the :ref:`course-materials`, :ref:`design-patterns` and :ref:`delivery-patterns` to guide the design and delivery of future sessions. While the module-level cycle focuses on immediate adaptations, the course-level cycle takes a more strategic view across multiple sessions and cohorts.

.. todo::

   TODO: Improve course level PDCA cycle

   .. graphviz::
      :align: center
      :alt: Course level PDCA Cycle
      :caption: Course level PDCA Cycle

      digraph PDCA {
         rankdir=TB;
         compound=true;
         splines=true;
         node [shape=box, style="rounded,filled", fontsize=11, fontname="Arial"];
         edge [fontsize=10, fontname="Arial"];

         E [label="Identify opportunities,\nCategorize & review observations,\nPrioritize updates", fillcolor="white"];
         F [label="Make improvements,\nUpdate course materials", fillcolor="white"];
         G [label="Review improvements", fillcolor="white"];
         H [label="Release new version,\nCommunicate changes", fillcolor="white"];
         
         E -> F -> G -> H;
         H -> E [constraint=false];
      }
      }

Plan
++++

The planning stage at the course level involves a comprehensive review of accumulated observations and feedback to identify strategic improvement opportunities.

**Identify opportunities for improvement** where the course designer reviews the observations and requirements for improvement. These requirements might come from the session observations, participant feedback, a more strategic review of the course, or other sources. The designer considers these in relation to the learning intentions, looking beyond simple fixes to identify deeper opportunities to enhance the learning journey.

**Categorise observations** Given the number of observations that we collect, it is helpful to categorise and tag them so we can better understand the patterns and trends, and decide which aspects to focus on. This qualitative analysis helps us identify recurring themes that might not be apparent in individual session reviews.

**Review observations** to understand the patterns and trends across the observation dataset. Sometimes there may be conflicting observations, due to different perspectives or interpretations. We will document any relevant variations or alternative approaches in the pattern documentation and delivery guidance. This process honors the subjective nature of the learning experience while seeking actionable insights.

**Prioritise updates** based on the importance of the observations and the impact of the changes. Some observations can be addressed immediately, while others may be part of a longer-term plan or need further evidence or research before we can make changes. We prioritize changes that most significantly enhance the realization of learning intentions rather than simply addressing logistics.

Do 
++

The implementation stage takes prioritized improvements and develops them into course enhancements.

**Make improvements** where the course designer identifies the changes to the course design and delivery that are needed to address the requirements. This involves creative problem-solving and pattern development rather than just fixing issues.

**Update course materials** We will make major and minor updates to the course materials, patterns and guidance based on the observations and feedback. Note that we will test significant updates before releasing a new version. Our materials evolve to better support the learning journey while maintaining consistency in core elements.

Check
++++

The check stage evaluates changes before wider implementation.

**Review the improvements** where changes are tested and reviewed to ensure they have the desired effect. This might overlap with the session level PDCA cycle. We look specifically at how changes impact the participant experience and their progress toward learning intentions, rather than just smooth delivery.

Act
+++

The act stage formalizes and communicates the improvements.

**Release new version** A new version of the course materials, patterns and guidance is released after testing. Version control ensures clarity about which materials should be used for upcoming deliveries.

**Communicate changes** to the Faculty and our community. We will also update this website for the latest release of course materials, patterns and guidance. Communication includes not just what changed but why, connecting improvements to learning intentions and participant experience.

Feedback integration in the improvement process
-----------------------------------------------

Integrating diverse feedback sources provides a rich, qualitative dataset that guides both immediate session adjustments and longer-term course evolution.

Participant feedback provides important insights into the subjective experience of learning. This includes both formal feedback through surveys, and informal feedback through conversations, chat messages, and observed behaviors. We pay special attention to stories of application and impact, as these often reveal the most meaningful aspects of the learning experience.

Delivery team feedback comes from facilitators, producers, and observers who experience the session from different perspectives. Their observations capture both a perspective on participant engagement and the behind-the-scenes elements that support successful delivery.

Stakeholder feedback, including from community members, sponsors and participant managers, helps us understand the broader context and impact of the learning. This feedback often reveals how learning transfers to real-world applications and what organizational factors influence success.

We adapt our observation and feedback approaches to focus attention on emerging areas of interest.

-----------------------------------------------
:material-outlined:`groups;1.8rem` Design roles
-----------------------------------------------

The following roles are involved in the continuous improvement process:

- **Delivery Team:** This includes facilitators, producers, observers and sponsors and anyone training in those roles in the sessions.
- **Course Designers:** Creates the learning journey
- **Content Developer:** Develops and maintains materials


----------------------------------------------------------------
:material-outlined:`content_paste;1.8rem` Examples and resources
----------------------------------------------------------------

Common variations
-----------------

- **Rapid iteration cycles for urgent issues** These are needed for urgent issues that need to be addressed. We may need to update the flight plans during the session briefing and make changes to the master versions of the flight plans later.
- **Periodic comprehensive reviews** We will review the course materials and patterns to ensure they are up to date and aligned with the latest research and practice.
- **Continuous small enhancements** We will make small changes to the course materials and patterns to improve the learning experience.   
- **Major version updates** Sometimes, we may need to make significant changes to the course materials and patterns to address new research or practice. We will communicate the likely changes in advance to our Faculty and Community to allow them to prepare for the changes.

Examples and resources
-----------------------

We use project management tools to help us manage the continuous improvement process. Examples of tools we use or have used include `Linear <https://linear.app>`_, `Trello <https://trello.com>`_, `Notion <https://notion.so>`_ and `Jira <https://www.atlassian.com/software/jira>`_.

It is not necessary to use specialist software to manage the CI process. When we piloted the course we used standard word processing documents and/or spreadsheets such as Microsoft Word and Excel or Google Docs and Sheets. We moved to more sophisticated tools as we scaled up to deliver more sessions.

------------------------------------------------------------
:material-outlined:`touch_app;1.8rem` Setup and requirements
------------------------------------------------------------

Further information about the setup and requirements for the CI process are available in the following  patterns.

- Observation forms (see :ref:`observations-delivery-pattern`)
- Approaches for improving the course design and delivery (see :ref:`continuous-improvement-pattern`)

.. todo::

   TODO: Update additional design factors

   -------------------------------------------------------------------
   :material-outlined:`sticky_note_2;1.8rem` Additional design factors
   -------------------------------------------------------------------  

   Implementation considerations
   -----------------------------

   - Change impact assessment
   - Resource allocation balance
   - Implementation timing
   - Validation methodology
   - Documentation standards
   - Knowledge sharing practices

   Design evolution
   ---------------

   - Pattern integration strategies
   - System-wide improvement approaches
   - Long-term enhancement planning
   - Continuous learning framework
   - Pattern repository management

----------------------------------------------------
:material-outlined:`sync;1.8rem` Improvement process
----------------------------------------------------

Of course the CI pattern can be applied to improve the CI process itself!

-------------------------------------------
:material-outlined:`book;1.8rem` References
-------------------------------------------

Related Patterns:

- :ref:`observations-design-pattern`
- :ref:`observations-delivery-pattern`
- :ref:`flight-plan-design-pattern`
- :ref:`flight-plan-delivery-pattern`
- :ref:`roles-design-pattern`
- :ref:`roles-delivery-pattern`
- :doc:`Technical documentation </documentation/index>`
