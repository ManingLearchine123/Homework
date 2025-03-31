document.addEventListener("DOMContentLoaded", () => {
    // Form validation
    const loginForm = document.getElementById("login-form")
  
    loginForm.addEventListener("submit", (event) => {
      event.preventDefault()
  
      const username = document.getElementById("username").value
      const password = document.getElementById("password").value
  
      if (!username || !password) {
        alert("Please fill in all required fields")
        return
      }
  
      // This is where you would normally send the login request to a server
      // For demo purposes, we'll just show an alert
      alert("Login attempt with username: " + username)
  
      // Clear form fields after submission
      loginForm.reset()
    })
  
    // Add GitHub icon fallback in case Font Awesome doesn't load
    const checkFontAwesome = setTimeout(() => {
      const githubButton = document.querySelector(".btn-github")
      if (githubButton && !document.querySelector(".fa-github")) {
        githubButton.innerHTML = "⚙️ Log in with GitHub"
      }
      
  
      const twitterIcon = document.querySelector(".fa-twitter")
      if (!twitterIcon) {
        document.querySelectorAll(".social-icon")[0].innerHTML = "🐦"
      }
  
      const facebookIcon = document.querySelector(".fa-facebook-f")
      if (!facebookIcon) {
        document.querySelectorAll(".social-icon")[1].innerHTML = "📘"
      }
    }, 1000)
  })
  
  