function validateMemberIdUsingAjax() {
  let referral = document.getElementById('referral_id').value.trim()
  let referral_name = document.getElementById('referral_name_warning')


  if (referral.length == 0){
    referral_name.classList.add('d-none')
    return false
  }


  referral_name.classList.remove('d-none')
  // Make an Ajax request
  let xhr = new XMLHttpRequest()
  xhr.open('POST', '/main/get_sponsor_name/', true)
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let response = JSON.parse(xhr.responseText)
      
      // Handle the response
      if (response.name) {
        referral_name.textContent = "Sponsor: "+response.name
        referral_name.style.color = "green"
      } else {
        referral_name.textContent = "Sponsor Does Not Exist"
        referral_name.style.color = "red"
      }
    }
    else{
      referral_name.textContent = "Server Error"
      referral_name.style.color = "red"
    }
  }

  // Send the request with the referral data
  xhr.send('sponsor_id=' + encodeURIComponent(referral))
}

document.getElementById('referral_id').onkeyup = validateMemberIdUsingAjax
