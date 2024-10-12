==========
Contact Us
==========

You can contact our support team by clicking the button below.

.. raw:: html

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>

    <button id="zammad-feedback-form">Submit a request to our support team</button>

    <script id="zammad_form_script" src="https://support.betterconversations.foundation/assets/form/form.js"></script>

    <script>
    $(function() {
      $('#zammad-feedback-form').ZammadForm({
        messageTitle: 'Contact Us',
        messageSubmit: 'Submit',
        messageThankYou: 'Thank you for your inquiry (#%s)! We\'ll contact you as soon as possible.',
        showTitle: true,
        modal: true,
        attachmentSupport: true
      });
    });
    </script>

-----
Email
-----

Alternatively, you can email us at hello@betterconversations.foundation. 
But the form above is more reliable as it won't get lost in spam filters. 

