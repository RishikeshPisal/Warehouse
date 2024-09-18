
function validateMemberIdUsingAjax() {
  // remove the warning at the time of form-filling
  const warning = document.getElementById('fix-errors')
  warning.classList.add('d-none')

  const member_id = document.getElementById('member-id').value.trim()
  const member_name = document.getElementById('member-warning')

  if (member_id.length == 0){
    member_name.classList.add('d-none')
    return false
  }
  
  member_name.classList.remove('d-none')
  if (member_id === document.getElementById('current-user').value){
    member_name.textContent = "Can't send amount to yourself"
    member_name.style.color = 'red'
    return
  }
  // Make an Ajax request
  let xhr = new XMLHttpRequest()
  xhr.open('POST', '/member/get_sponsor_name/', true)
  xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded')
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      let response = JSON.parse(xhr.responseText)
      
      // Handle the response
      if (response.name) {
        member_name.textContent = "Member: "+response.name
        member_name.style.color = "green"
      } else {
        member_name.textContent = "Member Does Not Exist"
        member_name.style.color = "red"
      }
    }
    else{
      member_name.textContent = "Server Error"
      member_name.style.color = "red"
    }
  }

  // Send the request with the sponsor_id data
  xhr.send('sponsor_id=' + encodeURIComponent(member_id))
}


function calculateAmount(){
  // remove the warning at the time of form-filling
  const warning = document.getElementById('fix-errors')
  warning.classList.add('d-none')

  const transactionalChargesPerecentage = Number(document.getElementById('transactonal-charges-percentage').value)
  const balance = document.getElementById('balance').value
  const transactionalChargesElement = document.getElementById('transaction-charges')
  const amount = Number(document.getElementById('amount').value)
  const amountWarning = document.getElementById('amount-warning')


  const transactionalCharges = (amount*transactionalChargesPerecentage)/100
  const availableAmountElement = document.getElementById('available-amount')

  if (amount+transactionalCharges > balance){
    amountWarning.classList.remove('d-none')
    amountWarning.innerText = "Insufficient Balance"
    amountWarning.style.color = "red"
  }
  else{
    amountWarning.classList.add('d-none')
    availableAmountElement.value = balance-amount-transactionalCharges
    transactionalChargesElement.value = transactionalCharges
  }
}
function calculateAmountInWDR(){
  // remove the warning at the time of form-filling
  const warning = document.getElementById('fix-errors-in-wdr')
  warning.classList.add('d-none')

  const balance = document.getElementById('balance').value
  const transactionalChargesElement = document.getElementById('withdrawal-charges')
  const amountWarning = document.getElementById('amount-warning-in-wdr')
  const transactionalChargesPerecentage = Number(document.getElementById('withdrawal-charges-percentage').value)
  const amount = Number(document.getElementById('amount-in-wdr').value)
  const minimumAmount = Number(document.getElementById('minimum-withdrawal-amount').value)
  console.log(minimumAmount);
  const transactionalCharges = (amount*transactionalChargesPerecentage)/100
  const availableAmountElement = document.getElementById('available-amount-in-wdr')

  if (amount+transactionalCharges > balance){
    amountWarning.classList.remove('d-none')
    amountWarning.innerText = "Insufficient Balance"
    amountWarning.style.color = "red"
    availableAmountElement.value = balance
    transactionalChargesElement.value = 0
  }
  else if (amount < minimumAmount){ // change minimum amount later
    amountWarning.classList.remove('d-none')
    amountWarning.innerText = `Minimum Withdrawal is ${minimumAmount}`
    amountWarning.style.color = "red"
    availableAmountElement.value = balance
    transactionalChargesElement.value = 0
  }
  else{
    amountWarning.classList.add('d-none')
    transactionalChargesElement.value = transactionalCharges
    availableAmountElement.value = balance-amount-transactionalCharges
  }
}


document.getElementById('member-id').onkeyup = validateMemberIdUsingAjax
const fundTransferForm = document.getElementById('fund-transfer-form')
document.getElementById('fund-transfer-btn').addEventListener('click',()=>showSwal('fund-transfer',fundTransferForm))
const withdrawalRequestForm = document.getElementById('withdrawal-request-form')
document.getElementById('withdrawal-request-btn').addEventListener('click',()=>showSwal('withdrawal-request',withdrawalRequestForm))
