const client_id = '9cab658883ca4640b7ab8ad464548190';
const client_secret = 'a26bea8958574f6b89704a358c51fff3';

async function getToken() {
    const response = await fetch('https://accounts.spotify.com/api/token', {
        method: 'POST',
        body: new URLSearchParams({
            'grant_type': 'client_credentials',
        }),
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic ' + btoa(client_id + ':' + client_secret),
        },
    });

    const data = await response.json();
    return data.access_token;
}

async function getTrackInfo(access_token) {
    const response = await fetch('https://api.spotify.com/v1/tracks/4cOdK2wGLETKBW3PvgPWqT', {
        method: 'GET',
        headers: { 'Authorization': 'Bearer ' + access_token },
    });

    return await response.json();
}

getToken().then(access_token => {
    getTrackInfo(access_token).then(profile => {
        console.log(access_token)
        console.log(profile);
    });
});