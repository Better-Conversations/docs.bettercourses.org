.. _technical-stack:

===============
Technical Stack
===============

If you're interested in the technical details of how this website and the
Foundation's content is run... here's the breakdown.

Where possible we self-host to keep costs down, and leverage Amphora's 
existing infrastructure. 

Generally our infrastructure is managed by our sponsor, Amphora Research Systems Ltd.
We do have a separate GitHub organisation for the Foundation, which is here: https://github.com/Better-Conversations.
This has all the public repositories like this web site. 

The coordinator is in the Amphora GitHub organisation, mainly so we don't have
to pay twice for a lot of tools we use and already have in place in Amphora. 


---------
Web Sites
---------

The Foundation's web site is built using Astro, GitHub repository here
https://github.com/Better-Conversations/betterconversations.foundation,
served by Caddy on one of our servers.

The documentation website is built using Sphinx, GitHub repository here
https://github.com/Better-Conversations/betterconversations.foundation,
served by Caddy on one of our servers.

The web site bettercourses.org makes everything work. It does all the scheduling, enrolment, delivery console, certificates, etc.
This was built in-house by Amphora in Ruby on Rails.

Web site analytics is via the privacy-preserving https://umami.is/ which we self-host. We have a 
standard cookie consent on the web sites because people expect it but we're not
sure we really need it. 


------------
Flight Plans
------------

The course Flight Plans are here https://github.com/Better-Conversations/flightplan-sources

The flight plans use a custom DSL which is here https://github.com/Better-Conversations/ruby-flightplans

The "Active Flight Plans" app is a custom Rails app built by Amphora in Ruby on Rails. It takes 
the flight plans and gives a delivery and producer console for the delivery team to use.

When you order a copy of the flight plans in bettercourses.org, we use the Active Flight Plans app 
to generate the PDFs and send them to you. This allows us to customise them to your requirements. 

The flight plans are shipped to you as PDFs, if you want to edit them you can just open the PDF in Word.

--------------
Other Elements
--------------

Our community is run on Discourse, https://community.betterconversations.foundation with authentication via bettercourses.org

Our support is run in Help Scout in the same instance as Amphora's. 

We use Google Workspace for email and calendar, and Calendly for scheduling.

Tailscale stitches everything together. GitHub actions deploy the web sites to our Cloud servers.

Our Cloud servers are via Hetzner on their stunningly good value Arm-based VPS. 

Badges etc. for LinkedIn are issued via Open Badge Factory.

