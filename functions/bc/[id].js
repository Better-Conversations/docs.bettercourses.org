// This is a Cloudflare Pages Function to redirect from the /bc/ paths here to the /r/bc- paths on bettercourses.org
export async function onRequest(context) {
    const id = context.params.id;
    const redirectUrl = `https://bettercourses.org/r/bc-${id}`;
    return Response.redirect(redirectUrl, 302);
}
