function validateMemberInActivateMember() {
    // remove the warning at the time of form-filling
    const warning = document.getElementById('fix-errors-in-am')
    warning.classList.add('d-none')

    const member_id = document.getElementById('member-id-in-am').value.trim()
    const member_name = document.getElementById('member-warning-in-am')
    const fixErrorsWarning = document.getElementById('fix-errors-in-am')
    if (member_id.length == 0) {
        member_name.classList.add('d-none')
        return false
    }

    member_name.classList.remove('d-none')
    if (member_id === document.getElementById('current-user').value) {
        member_name.textContent = "Can't send amount to yourself"
        member_name.style.color = 'red'
        return
    }
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
function validateMemberInTransferEpins() {
    // remove the warning at the time of form-filling
    const warning = document.getElementById('fix-errors')
    warning.classList.add('d-none')

    const member_id = document.getElementById('member-id-in-te').value.trim()
    const member_name = document.getElementById('member-warning-in-te')

    if (member_id.length == 0) {
        member_name.classList.add('d-none')
        return false
    }

    member_name.classList.remove('d-none')
    if (member_id === document.getElementById('current-user').value) {
        member_name.textContent = "Can't send amount to yourself"
        member_name.style.color = 'red'
        return
    }
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

function checkPackageInAM() {
    const packageElement = document.getElementById('package-in-am')
    const packageWarning = document.getElementById('package-warning-in-am')
    const errorsParagraph = document.getElementById('fix-errors-in-am')
    if (packageElement.options[packageElement.selectedIndex].text !== '-' && errorsParagraph.classList.contains('d-none')) 
    {
        errorsParagraph.classList.add('d-none')
        return true
        
    }else{
        errorsParagraph.classList.remove('d-none')
        return false
    }
    
}
function checkPackageInTE() {
    const packageElement = document.getElementById('package-in-te')
    const packageWarning = document.getElementById('package-warning-in-te')
    const errorsParagraph = document.getElementById('fix-errors-in-te')
    if (packageElement.options[packageElement.selectedIndex].text !== '-' && errorsParagraph.classList.contains('d-none')) 
    {
        errorsParagraph.classList.add('d-none')
        return true
        
    }else{
        errorsParagraph.classList.remove('d-none')
        return false
    }

}
function checkCount() {
    countElement = document.getElementById('count-in-te')
    // console.log(countElement,Number(countElement.value));
    countWarning = document.getElementById('count-warning-in-te')
    packageCount = Number(document.getElementById('package-in-te').selectedOptions[0].dataset.count)
    if (Number(countElement.value) <= packageCount){
        countWarning.classList.add('d-none')
    }
    else{
        countWarning.classList.remove('d-none')
        console.log('in count validation',countElement.value,packageCount);
        
    }
    // add validations
}
activateMemberForm = document.getElementById('activate-member-form')
document.getElementById('activate-member-btn').onclick = () => showSwal('activate-member', activateMemberForm)
transferEpinsForm = document.getElementById('transfer-epins-form')
document.getElementById('transfer-epins-btn').onclick = () => showSwal('transfer-epins', transferEpinsForm)
requestEpinsForm = document.getElementById('request-epins-form')
document.getElementById('request-epins-btn').onclick = () => showSwal('request-epins', requestEpinsForm)

document.getElementById('package-in-am').onchange = checkPackageInAM
document.getElementById('package-in-te').onchange = checkPackageInTE
document.getElementById('count-in-te').onkeyup = checkCount