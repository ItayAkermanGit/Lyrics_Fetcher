async function getLyrics(){
    const artist = document.getElementById('artist').value;
    const title = document.getElementById('title').value;
    const result = document.getElementById('result');

    try{
        const response = await fetch('/get-lyrics', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ artist, title })
        });

        const data = await response.json();

        if (data.lyrics){
            result.innerText = data.lyrics;
            result.style.display = 'block';
        } else{
            result.innerText = data.error;
            result.style.display = 'block';
        }
    } catch (err){
        result.innerText = "Error connecting to the server";
        result.style.display = 'block';
    }
}