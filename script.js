
async function checkPlagiarism() {
    const text = document.getElementById('text-input').value;
    const response = await fetch('/check', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text })
    });
    const result = await response.json();
    document.getElementById('result').innerText = 'Plagiarism Score: ' + result.score + '%';
}
