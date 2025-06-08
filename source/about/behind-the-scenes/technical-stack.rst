.. _technical-stack:

===============
Technical Stack
===============

If you're interested in the technical details of how this website and the
Foundation's content is run...

- The website is built using Sphinx, GitHub repository here
  https://github.com/Better-Conversations/betterconversations.foundation,
  served by Caddy on one of our servers.
- The course Flight Plans are here https://github.com/Better-Conversations/flightplan-sources
- The flight plans use a custom DSL which is here https://github.com/Better-Conversations/ruby-flightplans
- The web site bettercourses.org makes everything work. It does all the scheduling, enrolment, delivery console, certificates, etc.
  This was build in-house by the Better Conversations Foundation in Ruby on Rails.
- Our community is run on Discourse, https://community.betterconversations.foundation with authentication via bettercourses.org
- Our support is run on Zammad, https://support.betterconversations.foundation with authentication via bettercourses.org
