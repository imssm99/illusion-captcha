const SERVER_URL = "http://localhost:8001"

async function illusion_captcha_install(size, on_success) {
    const div = document.getElementById("illusion_captcha");

    let resp = await (await fetch(`${SERVER_URL}/init?size=${size}`)).json()
    const question = resp.question
    const token = resp.token
    const len = resp.len

    div.innerHTML += `<p>${question}</p>`

    const handle = async (e) => {
        const idx = e.target.getAttribute("idx")

        resp = await (await fetch(`${SERVER_URL}/check`, {method: "POST", headers: {"Content-Type": "application/json"}, body: JSON.stringify({token: token, answer: idx})})).json()
        if(resp.status)
            on_success(token)
        else {
            alert("Failed!")
            location.reload()
        }
    }

    for(let idx = 0; idx < len; idx++) { 
        const img = new Image()
        img.src = `${SERVER_URL}/image/${idx}?token=${token}`
        img.onclick = handle
        img.setAttribute("idx", idx)
        div.appendChild(img)
    }

}
