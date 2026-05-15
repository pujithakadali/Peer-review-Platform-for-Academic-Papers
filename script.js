let token = "";

function login() {
  const username = document.getElementById("username").value;
  const password = document.getElementById("password").value;

  fetch("http://3.111.45.67:8000/api/token/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  })
    .then(res => res.json())
    .then(data => {
      token = data.access;
      localStorage.setItem("access", token);
      document.getElementById("login-status").innerText = "✅ Logged in!";
      fetchPapers();
    });
}

function uploadPaper() {
  const title = document.getElementById("title").value;
  const abstract = document.getElementById("abstract").value;

  fetch("http://3.111.45.67:8000/api/upload-paper/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer " + localStorage.getItem("access")
    },
    body: JSON.stringify({ title, abstract })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("upload-status").innerText = "✅ Paper uploaded!";
      fetchPapers();
    });
}

function fetchPapers() {
  fetch("http://3.111.45.67:8000/api/papers/")
    .then(res => res.json())
    .then(data => {
      const list = document.getElementById("paper-list");
      list.innerHTML = "";
      data.forEach(paper => {
        const li = document.createElement("li");
        li.className = "list-group-item";
        li.innerHTML = `<strong>${paper.title}</strong> - ${paper.abstract} 
          <a href="review.html" class="btn btn-sm btn-outline-primary ms-2">Review</a>`;
        list.appendChild(li);
      });
    });
}

window.onload = fetchPapers;
