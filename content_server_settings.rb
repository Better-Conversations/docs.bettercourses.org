class ContentServerSettings

    def settings
      # =============== URL ==================
      base_url = "https://betterconversations.foundation"
      site_identifier = "betterconversations.foundation"

      # =========== COMMENTING ===============
      commenting = "logged_in"

      # ============ TRACKING ================
      never_serve = [
        "_sources",
        "_ignore",
        'config.yml',
        'content_server_settings.rb',
        'development_autobuild.sh'
      ]

      dont_track = [
        "_sources",
        "static",
        '\.js',
        '\.png',
        '\.woff',
        '\.jpg',
        '\.css',
        'config.yml',
        '.ttf',
        '/assets/fonts/.*'
      ]

      access_mode = :public
      # access_mode_exceptions = [
      #   '/downloads/.*',
      #   'index.html',
      #   '/blog/.*',
      #   '/documentation/.*',
      #   '/booking/*',
      # ]

      # =========== FEATURES ===============
      views_on_page = true
      comment_section_name = "Discussion"
      search_bar = true
      sharing_link = false
      cc_sharing_link = false
      invite_link = false
      slack_webhook = "https://hooks.slack.com/services/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"

      html_content_locations = [
        "div[class='document']"
      ]

      url_redirect_list = {
        "https://betterconversations.foundation/l/license": "https://betterconversations.foundation/COPYRIGHT.html",
        "https://betterconversations.foundation/l/attribution": "https://betterconversations.foundation/work-with-us/crediting.html",
        "https://betterconversations.foundation/l/masters": "https://betterconversations.foundation/documentation/course-materials/flight_plans.html",
        "https://betterconversations.foundation/l/flightplans": "https://betterconversations.foundation/documentation/course-materials/flight_plans.html",
        "https://betterconversations.foundation/l/support": "https://betterconversations.foundation/documentation/course-materials/support.html",
        "https://betterconversations.foundation/l/zoombor": "https://betterconversations.foundation/documentation/design-patterns/Breakout-Rooms.html",
        "https://betterconversations.foundation/documentation/200-the_course.index.html": "https://betterconversations.foundation/course/index.html",
        "https://betterconversations.foundation/l/handbook": "https://betterconversations.foundation/downloads/BC%20Course%20Handbook.pdf",
        "https://betterconversations.foundation/documentation/800-resources/email-templates.html": "https://betterconversations.foundation/documentation/course-materials/email_templates.html",
        "https://betterconversations.foundation/l/overview": "https://betterconversations.foundation/documentation/downloads/v2.0/BCF%20BCO%20Course%20Overview%20v2.0.pdf",
        "https://betterconversations.foundation/2023/05/02/modelling-sales.html": "https://betterconversations.foundation/blog/2023-05-02-modelling-sales.html",        "https://betterconversations.foundation/thanks/index.html": "https://betterconversations.foundation/about/appreciation.html",

        "https://betterconversations.foundation/bc/alexc": "https://bettercourses.org/r/bc-alexc",
        "https://betterconversations.foundation/bc/joshuac": "https://bettercourses.org/r/bc-joshuac",
        "https://betterconversations.foundation/bc/shivanip": "https://bettercourses.org/r/bc-shivanip",
        "https://betterconversations.foundation/bc/saram": "https://bettercourses.org/r/bc-saram",
        "https://betterconversations.foundation/bc/simonc": "https://bettercourses.org/r/bc-simonc",
        "https://betterconversations.foundation/bc/chandimad": "https://bettercourses.org/r/bc-chandimad",
        "https://betterconversations.foundation/bc/danp": "https://bettercourses.org/r/bc-danp",


      }

      # high_value_alerts = [
      #   ".pdf",
      #   ".zip"
      # ]

      # =========== SITE MAP ===============
      exclude_from_sitemap = [
        ".doctree",
      ]

      # ============= SAML =================
      idp_sso_target_url = "https://bettercourses.org/sso/bcf_website"
      idp_cert_fingerprint = "BB:E5:6F:57:28:3E:69:0B:54:83:06:10:C4:AD:DA:2D:55:72:86:B3:5C:82:05:E4:40:C2:91:21:06:6A:42:B9"

      # ========= END OF CONFIG ===========
      # Return all local variables in this file as a hash
      return local_variables.each_with_object({}) { |key, hash| hash[key] = eval(key.to_s) }
    end
  end
