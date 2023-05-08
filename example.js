// Creating a new user
fetch('http://127.0.0.1:5000/create_user', {
  method: 'POST',
  body: new URLSearchParams({username: 'exampleUser'})
})
  .then(response => response.json())
  .then(console.log);

// Saving user data
fetch('http://127.0.0.1:5000/save_data', {
  method: 'POST',
  body: new URLSearchParams({
    username: 'exampleUser',
    trees: ['oak', 'maple'],
    co2_collected: 50
  })
})
  .then(response => response.json())
  .then(console.log);

// Visiting another user
fetch('http://127.0.0.1:5000/visit_user/exampleUser')
  .then(response => response.json())
  .then(console.log);
