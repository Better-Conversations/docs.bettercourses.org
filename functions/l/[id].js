// This is a Cloudflare Pages Function to redirect any stable links which begin with /l/ 

export async function onRequest(context) {
    const id = context.params.id;
    const redirects = {
        "license": "https://betterconversations.foundation/COPYRIGHT.html",
        "attribution": "https://betterconversations.foundation/work-with-us/crediting.html",
        "masters": "https://betterconversations.foundation/documentation/course-materials/flight_plans.html",
        "flightplans": "https://betterconversations.foundation/documentation/course-materials/flight_plans.html",
        "support": "https://betterconversations.foundation/documentation/course-materials/support.html",
        "zoombor": "https://betterconversations.foundation/documentation/design-patterns/Breakout-Rooms.html",
        "handbook": "https://betterconversations.foundation/downloads/BC%20Course%20Handbook.pdf",
        "overview": "https://betterconversations.foundation/downloads/BC%20Course%20Overview.pdf",
    }
    return Response.redirect(redirects[id], 302);
}



