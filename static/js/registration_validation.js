

// function validateSponsorIdUsingAjax() {
//   let sponsor_id = document.getElementById('sponsor_id').value.trim()
//   let sponsor_name = document.getElementById('sponsor_name_warning')
//   let token = document.getElementsByName('csrfmiddlewaretoken')[0]
//   console.log(token)

//   if (sponsor_id.length == 0){
//     sponsor_name.classList.add('d-none')
//     return false
//   }


//   sponsor_name.classList.remove('d-none')

  
//   fetch('get_sponsor_name', {
//     method: 'POST',
//     headers: {
//       'Content-Type': 'application/x-www-form-urlencoded',
//     },
//     body: {
//       'sponsor_id' : encodeURIComponent(sponsor_id),
//       'csrfmiddlewaretoken' : encodeURIComponent(sponsor_id)
//     }
//   })
//     .then(response => {
//       if (!response.ok) {
//         throw new Error('Server Error')
//       }
//       return response.json()
//     })
//     .then(data => {
//       // Handle the response
//       if (data.name) {
//         sponsor_name.textContent = "Sponsor: " + data.name
//         sponsor_name.style.color = "green"
//       } else {
//         sponsor_name.textContent = "Sponsor Does Not Exist"
//         sponsor_name.style.color = "red"
//       }
//     })
//     .catch(error => {
//       sponsor_name.textContent = "Server Error"
//       sponsor_name.style.color = "red"
//       console.error('Fetch error:', error)
//     })
  
// }

function validateSponsorIdUsingAjax() {
  let sponsor_id = document.getElementById('sponsor_id').value.trim()
  let sponsor_name = document.getElementById('sponsor_name_warning')


  if (sponsor_id.length == 0){
    sponsor_name.classList.add('d-none')
    return false
  }


  sponsor_name.classList.remove('d-none')
  // Make an Ajax request
  let xhr = new XMLHttpRequest()
  xhr.open('POST', '/main/get_sponsor_name/', true)
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let response = JSON.parse(xhr.responseText)
      
      // Handle the response
      if (response.name) {
        sponsor_name.textContent = "Sponsor: "+response.name
        sponsor_name.style.color = "green"
      } else {
        sponsor_name.textContent = "Sponsor Does Not Exist"
        sponsor_name.style.color = "red"
      }
    }
    else{
      sponsor_name.textContent = "Server Error"
      sponsor_name.style.color = "red"
    }
  }

  // Send the request with the sponsor_id data
  xhr.send('sponsor_id=' + encodeURIComponent(sponsor_id))
}
// These functions are used when the user leaves the field
function validateFullName(){
  let full_name = document.getElementById("full_name").value.trim()
  let error = document.getElementById("full_name_warning")
  if (full_name.length < 3){
    error.classList.remove("d-none")
    return false
  }
  else{
    error.classList.add("d-none")
    return true
  }
}
function validateMobileNo(){
  let mobile_no = document.getElementById("mobile_no").value.trim()
  let error = document.getElementById("mobile_no_warning")
  if (mobile_no.length==0) return 
  if (mobile_no.length != 10){
    error.classList.remove("d-none")
    return false
  }
  else{
    error.classList.add("d-none")
    return true
  }
}
function validateEmail(){
  let email_id = document.getElementById("email_id").value.trim()
  let error = document.getElementById("email_id_warning")
  if (email_id.match(/^(([^<>()[\]\\.,:\s@\"]+(\.[^<>()[\]\\.,:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)){
    error.classList.add("d-none")
    return true
  }
  else{
    error.classList.remove("d-none")
    return false
  }
}

// These functions are used while the user is typing
function validatePassword(){
  let password = document.getElementById("password").value
  let confirm_password = document.getElementById("confirm_password").value
  let error = document.getElementById("confirm_password_warning")
  if (!password){
    document.getElementById('password_warning').classList.remove("d-none")
    return false
  }
  else{
    document.getElementById('password_warning').classList.add("d-none")

  }
  if (password && confirm_password && password === confirm_password){
    error.classList.add("d-none")
    return true
  }
  else{
    error.classList.remove("d-none")
    return false
  }
}
function checkEmail(){
  let email_id = document.getElementById("email_id").value.trim()
  let email_id_warning = document.getElementById("email_id_warning")
  if (email_id.match(/^(([^<>()[\]\\.,:\s@\"]+(\.[^<>()[\]\\.,:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/))
    email_id_warning.classList.remove("d-none")
}

function validateDob() {
  // Get the value from the date of birth input
  let dob_value = document.getElementById('dob').value
  let dob_warning = document.getElementById('dob_warning')

  let dob_date = new Date(dob_value)

  let current_date = new Date()

  let age = current_date.getFullYear() - dob_date.getFullYear()
  // Check if the user is 18 or older
  if (age <= 18) {
    dob_warning.classList.remove('d-none')
    return false
  } else {
    dob_warning.classList.add('d-none')
    return true
  }
}
function handleSubmit(){
  let errors = ""
  if (document.getElementById("sponsor_id").value.trim().length == 0){
    let sponsor_name_warning = document.getElementById("sponsor_name_warning")
    sponsor_name_warning.classList.remove("d-none")
    sponsor_name_warning.style.color = "red"
    sponsor_name_warning.textContent = "Enter a sponsor id"
  }
  if (!validateFullName())
    errors += "Full Name Can't be less than 3 characters\n"
  if (!validateMobileNo())
    errors += "Invalid Mobile Number\n"
  if (!validateEmail())
    errors += "Invalid Email\n"
  if (!validatePassword())
    errors += "Password can't be empty and Both the passwords should be same\n"
  if (!validateDob())
    errors += "User can't be below 18 years\n"


  
  if (! errors){
    let form = document.getElementById("sign_up_form")
    form.submit()

  }
  else{
    // let warnings = document.getElementById("warnings")
    // warnings.classList.remove('d-none') 
    // warnings.textContent = errors
    console.log(errors)
  }
}



document.getElementById('sponsor_id').onkeyup = validateSponsorIdUsingAjax
document.getElementById('full_name').onblur = validateFullName
document.getElementById('full_name').onkeyup = validateFullName
document.getElementById('mobile_no').onblur = validateMobileNo
document.getElementById('mobile_no').onkeyup = validateMobileNo
document.getElementById('email_id').onblur = validateEmail
document.getElementById('email_id').onkeyup = validateEmail
document.getElementById('dob').onblur = validateDob
document.getElementById('confirm_password').onkeyup = validatePassword
document.getElementById("submit_button").onclick = handleSubmit


