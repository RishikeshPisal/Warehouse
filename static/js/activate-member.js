function validateMemberInActivateMember() {
  // remove the warning at the time of form-filling
  const warning = document.getElementById('member-warning')
  warning.classList.add('d-none')

  const member_id = document.getElementById('member-id').value.trim()
  const member_name = document.getElementById('member-warning')
  const fixErrorsWarning = document.getElementById('fix-errors')
  if (member_id.length == 0) {
      member_name.classList.add('d-none')
      return false
  }

  member_name.classList.remove('d-none')
  // Make an Ajax request
  let xhr = new XMLHttpRequest()
  xhr.open('POST', '/main/get_member_details/', true)
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
  xhr.onreadystatechange = function () {
      if (xhr.readyState === 4 && xhr.status === 200) {
          let response = JSON.parse(xhr.responseText)

          // Handle the response
          if (response.name) {
              member_name.textContent = "Member: " + response.name
              member_name.style.color = "green"
              if (!checkPackageInAm)
                  fixErrorsWarning.classList.remove('d-none')
              else{
                  fixErrorsWarning.classList.add('d-none')
                  console.log('here');
          }
          } else {
              member_name.textContent = "Member Does Not Exist"
              member_name.style.color = "red"
          }
      }
      else {
          member_name.textContent = "Server Error"
          member_name.style.color = "red"
      }
  }

  // Send the request with the sponsor_id data
  xhr.send('member_id=' + encodeURIComponent(member_id))
}
document.getElementById('package').addEventListener('change', function() {
    var selectedPackage = this.value;
    var epinSelect = document.getElementById('epin');
    var options = epinSelect.querySelectorAll('option');
    
    epinSelect.disabled = selectedPackage === '';

    options.forEach(function(option) {
        if (option.value === '') {
            option.selected = true;
            option.style.display = '';
        } else if (option.getAttribute('data-package') === selectedPackage) {
            option.style.display = '';
        } else {
            option.style.display = 'none';
        }
    });
});
document.getElementById('member-id').onkeyup = validateMemberInActivateMember