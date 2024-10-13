export async function onRequest(context) {
    const id = context.params.id;
    const redirectUrl = `https://bettercourses.org/r/bc-${id}`;
    return Response.redirect(redirectUrl, 302);
}
