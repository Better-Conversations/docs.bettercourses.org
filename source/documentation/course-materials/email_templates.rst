===============
Email Templates
===============

When we run our "Experience Courses" our system has some standard 
email templates. We've been asked to share them so here you are...

- The Invite Wording for each Module
- The follow up Fieldwork Wording for each Module
- Examples of our Pre- and Post-Session Emails
- Our Welcome Email

--------------
Invite Wording
--------------

Firstly, we have some standard wording for each module

Module 1 (State)
  To help you prepare for this module, think about conversations you would like to 
  be better as a result of this course.

  Can you give those conversations a name or a label to remember them easily?

  We will also explore a key factor in having Better Conversations - our State.

Module 2 (Assumptions)
  We'll be exploring how quickly and easily we make Assumptions, and the link to State.
      
  Please have a pen and some paper with you as we will be doing some drawing. Don't worry, there won't be a competition for best artwork!

Module 3 (Context)
  In this module, we will consider Context, and how you bring meaning to a conversation.

  To help you prepare, please think about a conversation you'd like to be better. What you would like to have happen in that conversation?

Module 4 (Listening with Curiosity)
  In this module, we will practice Listening with Curiosity, and how you can influence a conversation.

  To help you prepare, please think about a conversation you'd like to be better. What you would like to have happen in that conversation?


Module 5 (Intentional Conversations)
  This module introduces Intentional Conversations, and why our intentions for a conversation are only half the story.

  To help you prepare, please think about a conversation you'd like to be better. What you would like to have happen in that conversation?


-----------------
Fieldwork Wording
-----------------

After the session we send them an email "As a reminder here's the suggested fieldwork from the session"

Module 1 (State)
  - Notice your state, and how and when it changes for you.
  - Try mapping it to the Traffic Light Model.
  - What's your state like, before and after your conversations?

Module 2 (Assumptions)
  - Try noticing what you are seeing or hearing when you are interacting with someone.
  - What assumptions are you making in your interactions?
  -	Are your assumptions accurate?

Module 3 (Context)
  - Try noticing what context you bring to a conversation
  - What do you know about the other person’s context?
  - What impact does that have on the conversation?"

Module 4 (Listening with Curiosity)
  - Try out some of the questions on page 20 of the handbook in your conversations. 
  - What kind of listening do you do in a conversation?
  - What impact does that have on the conversation?"
  
Module 5 (Intentional Conversations)
  There is no fieldwork for Module 5. 


----------------------------
Pre- and Post-Session Emails
----------------------------

These are the emails we slot this text into. As you can see they
are very standardised and we've just copy and pasted from 
the app that runs bettercourses.org so there's still code in there.
But hopefully that makes it easier to see how it all fits together.


This is the email we send out before the session. It's a reminder of the session details, and the fieldwork from the session before.

.. code-block:: none

  Hi <%= @attendance.user.first_name %>,

  We hope you are excited for Module <%= @attendance.zoom_session.module_number %> of Better Conversations today.

  <% unless @module_text_prep.empty? %>
  <%= @module_text_prep %>
  <% end %>

  <% unless @module_text_prev_fieldwork.empty? %>
  <%= @module_text_prev_fieldwork %>
  <% end %>

  You can see the session details, join the Zoom meeting, download the
  handbook, and more here <%= live_view_attendance_url(uuid:
  @attendance.ical_uuid) %>

  If you have any problems or concerns on the day, you can contact us via
  email at hello@betterconversations.foundation or phone us on +44 118 234
  9811.

  See you in an hour!

  Best wishes,

  The Better Conversations Team


  (PS You can join the session using the link above, or directly <%=
  @attendance.zoom_session.zoom_link %>)



This is the email we send after the session.

.. code-block:: none
  
  Hi <%= @attendance.user.first_name %>,

  Thank you for attending today's session of Better Conversations, we hope
  you enjoyed it.

  <%= @module_text_fieldwork %>

  We look forward to seeing you at the next session. We'll send a reminder
  before then.

  Best wishes,

  The Better Conversations Team


-----------------
The Welcome Email
-----------------

This is our standard welcome email people get when they sign up. 

.. code-block:: none

  Hi <%= @user.first_name %>,

  Thank you for signing up for Better Conversations. You should have been
  taken to a page where you can book a course at time convenient to you.

  Note that all the times you see in emails from us and on the web site are
  in your local time zone, which we believe to be <%= @timezone %>. We will
  send calendar invites for the sessions you have booked with the Zoom
  meeting details.

  If that's wrong, or you have any questions, please do get in touch at
  hello@betterconversations.foundation. 

  To make the most of the course, we recommend doing a few things before
  each session:

  - Connect using a laptop or desktop device. Zoom functionality is limited
    on a mobile devices (such as access to the Chat function in Breakout
    Rooms)

  - Ensure you have the latest version of Zoom on your device

  - Join us from a quiet place where you are unlikely to be disturbed 

  - Make sure that we can see and hear you clearly as this is a interactive
    class. We can help with this if you join us 5-10 minutes before the
    session.

  - Make use of the automatic captions in Zoom. You can also view live
    transcriptions in languages supported by Zoom.

  We've compiled some tips for online meetings at
  https://betterconversations.foundation/documentation/public/Online%20Meeting%20Guidelines.pdf

  If you are unfamiliar with Zoom, you can find guidelines on joining a
  meeting at
  https://support.zoom.us/hc/en-us/articles/201362193-Joining-a-Zoom-meeting

  For more info on automated captions and live transcription please visit
  https://support.zoom.us/hc/en-us/articles/4403492514829-Viewing-captions-in-a-meeting-or-webinar



  Again, thank you for signing up and we hope you enjoy the course.


  Best Wishes, 

  The Better Conversations Team
