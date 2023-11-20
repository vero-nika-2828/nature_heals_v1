/*
    Core logic/payment flow comes from Stripe docs:
    https://stripe.com/docs/payments/accept-a-payment

    CSS from Stripe docs: 
    https://stripe.com/docs/stripe-js
*/

var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
var client_secret = $('#id_client_secret').text().slice(1, -1);