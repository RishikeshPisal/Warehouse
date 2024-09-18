(function($) {
  showSwal = function(type,form) {
    'use strict';
    // const fundTransferForm = document.getElementById('fund-transfer-form')
    if (type === 'basic') {
      swal({
        text: 'Any fool can use a computer',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'title-and-text') {
      swal({
        title: 'Read the alert!',
        text: 'Click OK to close this alert',
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'success-message') {
      swal({
        title: 'Congratulations!',
        text: 'You entered the correct answer',
        icon: 'success',
        button: {
          text: "Continue",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })

    } else if (type === 'auto-close') {
      swal({
        title: 'Auto close alert!',
        text: 'I will close in 2 seconds.',
        timer: 2000,
        button: false
      }).then(
        function() {},
        // handling the promise rejection
        function(dismiss) {
          if (dismiss === 'timer') {
            console.log('I was closed by the timer')
          }
        }
      )
    } else if (type === 'warning-message-and-cancel') {
      swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3f51b5',
        cancelButtonColor: '#ff4081',
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true
          }
        }
      })

    } else if (type === 'custom-html') {
      swal({
        content: {
          element: "input",
          attributes: {
            placeholder: "Type your password",
            type: "password",
            class: 'form-control'
          },
        },
        button: {
          text: "OK",
          value: true,
          visible: true,
          className: "btn btn-primary"
        }
      })
    } else if (type === 'withdrawal-request') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          submit: {
            text: "Submit",
            value: false,
            visible: true,
            className: "btn btn-success",
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
      })
      document.getElementsByClassName('swal-button--submit')[0].addEventListener('click',()=>{
        // remove the unnecessary loader
        const loader = document.getElementsByClassName('swal-button__loader')[0]
        if(loader) loader.remove()
        // perform validations
        const amount = document.getElementById('amount-in-wdr')
        const countWarning = document.getElementById('amount-warning-in-wdr')
        if (countWarning.classList.contains('d-none') && amount.value !== '' ){
          form.submit()
        }
        else{
          const warning = document.getElementById('fix-errors')
          warning.classList.remove('d-none')
          console.log('problem')
        }
      })
  
    } else if (type === 'fund-transfer') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          transfer: {
            text: "Transfer",
            value: false,
            visible: true,
            className: "btn btn-success",
            showLoaderOnConfirm:false,
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
     })
    //  make the tranfer button as submit button
     document.getElementsByClassName('swal-button--transfer')[0].addEventListener('click',()=>{
      // remove the unnecessary loader
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      if(loader) loader.remove()
      // perform validations
      const amount = document.getElementById('amount')
      const countWarning = document.getElementById('amount-warning')
      const member_name = document.getElementById('member-warning')
      if (countWarning.classList.contains('d-none') && amount.value !== '' && member_name.style.color == "green"){
        form.submit()
      }
      else{
        const warning = document.getElementById('fix-errors')
        warning.classList.remove('d-none')
      }

    })
    } else if (type === 'confirm-fund-transfer') {
      // do this later
      swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        buttons: {
          confirm: {
            text: "Confirm",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          },
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
        }
      })
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
        const fundTransferForm = document.getElementById('fund-transfer-form')
        const submitBtn = document.getElementById('fund-transfer-submit-btn')
        const formData = new FormData(fundTransferForm,submitBtn)
        console.log(formData.get('member-id'))
        
        // document.getElementById('fund-transfer-form').submit()
      })


    }
    else if (type === 'activate-member') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          submit: {
            text: "Activate",
            value: false,
            visible: true,
            className: "btn btn-success",
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
      })
      document.getElementsByClassName('swal-button--submit')[0].addEventListener('click',()=>{
        // remove the unnecessary loader
        const loader = document.getElementsByClassName('swal-button__loader')[0]
        if(loader) loader.remove()
        // perform validations
        const memberId = document.getElementById('member-id-in-am')
        const memberIdWarning = document.getElementById('member-warning-in-am')
        const packageElement = document.getElementById('package-in-am')
        const packageWarning = document.getElementById('package-warning-in-am')
        console.log(packageElement.options[packageElement.selectedIndex].value)
        if (
            memberId.value != '' &&
            memberIdWarning.style.color === 'green' && 
            packageWarning.classList.contains('d-none') && 
            packageElement.options[packageElement.selectedIndex].text !== '-'
        ){
          form.submit()
        }
        else{
          const warning = document.getElementById('fix-errors-in-am')
          warning.classList.remove('d-none')
        }
      })
    }
    else if (type === 'transfer-epins') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          submit: {
            text: "Transfer",
            value: false,
            visible: true,
            className: "btn btn-success",
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
      })
      document.getElementsByClassName('swal-button--submit')[0].addEventListener('click',()=>{
        // remove the unnecessary loader
        const loader = document.getElementsByClassName('swal-button__loader')[0]
        if(loader) loader.remove()
        // perform validations
        const count = document.getElementById('count-in-te')
        const countWarning = document.getElementById('count-warning-in-te')
        if (countWarning.classList.contains('d-none') && count.value !== '' ){
          form.submit()
          // console.log('done');
        }
        else{
          const warning = document.getElementById('fix-errors-in-te')
          warning.classList.remove('d-none')
          console.log('problem')
        }
      })
    }
    else if (type === 'request-epins') {
      if(form?.classList.contains('d-none'))
        form.classList.remove('d-none')
      swal({
        content: form,
        buttons: {
          submit: {
            text: "Send",
            value: false,
            visible: true,
            className: "btn btn-success",
            loaderHtml: '',
            closeModal: false,
          },
          cancel: {
            text: "Cancel",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true  
          }
        }
      })
      document.getElementsByClassName('swal-button--submit')[0].addEventListener('click',()=>{
        // remove the unnecessary loader
        const loader = document.getElementsByClassName('swal-button__loader')[0]
        if(loader) loader.remove()
        form.submit()

      })
    }
    else if (type === 'confirm-bill') {
      swal({
        title: 'Are you sure?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true
          }
        }
      })
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
      if(loader) loader.remove()
        console.log('okay');
        saveBill()

      })
    }
    else if (type === 'place-order') {
      swal({
        title: 'Place Order?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-danger",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-primary",
            closeModal: true
          }
        }
      })
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
      if(loader) loader.remove()
        console.log('okay');
        placeOrder()

      })
    }
    else if (type === 'reject-order') {
      swal({
        title: 'Reject Order?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true
          }
        }
      })
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
      if(loader) loader.remove()
        console.log('okay');
        document.getElementById('reject-order-link').click()
      })
    }
    else if (type === 'process-payout') {
      swal({
        title: 'Process Payout?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Great ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true
          }
        }
      })
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
      if(loader) loader.remove()
        document.getElementById('process-payout-link').click()
      })
    }
    else if (type === 'delete-rank') {
      swal({
        title: 'Delete Rank ?',
        text: "You won't be able to revert this!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Delete ',
        buttons: {
          cancel: {
            text: "Cancel",
            value: null,
            visible: true,
            className: "btn btn-primary",
            closeModal: true,
          },
          confirm: {
            text: "OK",
            value: true,
            visible: true,
            className: "btn btn-danger",
            closeModal: true
          }
        }
      })
      const loader = document.getElementsByClassName('swal-button__loader')[0]
      document.getElementsByClassName('swal-button--confirm')[0].addEventListener('click',()=>{
      if(loader) loader.remove()
        document.getElementById('delete-rank-link').click()
      })
    }
    else{
      console.log("Type not mentioned in alert.js")
    }
  }

})(jQuery);