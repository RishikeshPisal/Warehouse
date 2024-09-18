// Globals
table = document.getElementById('main-table')
tableBody = table.children[1]

// contains all the items in the invoice
items = {}


function addItem(that) {
  console.log(items);
  const select = document.getElementById('product-name')
  const product_id = document.getElementById('product-name').value
  const product_name = select.options[select.selectedIndex].text
  const quantity = (product_id) ? Number(document.getElementById(`quantity-${product_id}`).value) : 0

  // form without selecting product name is rejected
  if (!product_id || quantity == 0) {
    return
  }

  const stock = Number(document.getElementById(`product-stock-${product_id}`).dataset.value)
  const product_mrp = Number(document.getElementById(`product-mrp-${product_id}`).dataset.value)
  const product_bv = Number(document.getElementById(`product-bv-${product_id}`).dataset.value)
  // const product_pv = document.getElementById(`product-pv-${product_id}`).dataset.value
  const product_dp = Number(document.getElementById(`product-dp-${product_id}`).dataset.value)
  const product_gst_rate = Number(document.getElementById(`product-gst-${product_id}`).dataset.value)
  const product_gst_type = document.getElementById(`product-gst-type-${product_id}`).dataset.value

  const gst_amount = get_gst_value(product_dp, product_gst_rate)
  // const total_mrp_product = 
  // check if already in the list
  if (quantity > stock || items[product_id] + quantity > stock) {
    console.log('not enough');
    showWarningToast("You don't have enough stock !!!.")
    return
  }
  if (!items[product_id]) {
    document.getElementById('save-btn-strip').classList.remove('d-none')
    document.getElementById('save-btn-strip').classList.add('d-flex')
    document.getElementById('hidden-field-1').classList.remove('d-none')
    table.parentNode.classList.remove('d-none')

    // adds a new row
    tableBody.innerHTML +=
      ` <tr id='${product_id}'>
          <td>${tableBody.children.length + 1}</td>
          <td>${product_name}</td>
          <td>${quantity}</td>
          <td>${quantity * product_dp}</td>
          <td>${quantity * product_bv}</td>
          <td>
            ${(product_gst_type === 'INC') ? //if inclusive
        get_gst_value(product_dp, product_gst_rate, quantity)
        ://else
        (quantity * product_dp * product_gst_rate / 100)
      } (${product_gst_type})
          </td>
          <td>${quantity * product_mrp}</td>
          <td class=' delete-item-btn'onclick="deleteRow(this)" >
            <svg class='row m-auto' align='center' xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">
              <path d="M135.2 17.7L128 32H32C14.3 32 0 46.3 0 64S14.3 96 32 96H416c17.7 0 32-14.3 32-32s-14.3-32-32-32H320l-7.2-14.3C307.4 6.8 296.3 0 284.2 0H163.8c-12.1 0-23.2 6.8-28.6 17.7zM416 128H32L53.2 467c1.6 25.3 22.6 45 47.9 45H346.9c25.3 0 46.3-19.7 47.9-45L416 128z"/>
            </svg>
          </td>

        </tr>
      `
    items[product_id] = quantity

  } else { //if already in the list just increment the quantity and handle price
    items[product_id] += quantity
    document.getElementById(product_id).children[2].innerText = items[product_id]
    document.getElementById(product_id).children[3].innerText = product_dp * items[product_id]
    document.getElementById(product_id).children[4].innerText = product_bv * items[product_id]
    document.getElementById(product_id).children[5].innerText =
     `${(product_gst_type === 'INC') ? //if inclusive
        get_gst_value(product_dp, product_gst_rate, items[product_id])
        ://else
        (items[product_id] * product_dp * product_gst_rate / 100)
      } 
      (${product_gst_type})`
      
    document.getElementById(product_id).children[6].innerText = product_mrp * items[product_id]
  }
  console.log(items)
  // reset the stuff
  document.getElementById(`quantity-${product_id}`).value = 0
  select.selectedIndex = 0
  recalculateFooter()

  // form.reset();
}


function deleteRow(btn) {
  // Get the reference to the row containing the clicked button
  var row = btn.parentNode;


  // Delete the row from the table
  row.parentNode.removeChild(row);
  let i = 0
  // handle the sr.no
  while (i < tableBody.children.length) {
    tableBody.children[i].children[0].innerText = i + 1
    i++;
  }

  if (!tableBody.children.length) {
    table.parentNode.classList.add('d-none')
    document.getElementById('save-btn-strip').classList.add('d-none')
    document.getElementById('hidden-field-1').classList.add('d-none')
    // console.log(row.id)
  }
  delete items[row.id]
  console.log(items)
  recalculateFooter()
}
function get_gst_value(dp, rate, quantity = 1) {
  rate = Number(rate)
  dp = Number(dp)
  const value = Math.round((quantity * dp * rate) / (100 + rate) * 100) / 100
  console.log(value)
  return value
}

function recalculateFooter() {
  const keys = Object.keys(items)
  let total_bv = 0
  let total_mrp = 0
  let total_dp = 0
  let total_items = 0
  let total_gst = 0
  for (let i = 0; i < keys.length; i++) {

    const bv = Number(document.getElementById(`product-bv-${keys[i]}`).dataset.value)
    // const pv = Number(document.getElementById(`product-pv-${keys[i]}`).dataset.value)
    const dp = Number(document.getElementById(`product-dp-${keys[i]}`).dataset.value)
    const mrp = Number(document.getElementById(`product-mrp-${keys[i]}`).dataset.value)
    const rate = Number(document.getElementById(`product-gst-${keys[i]}`).dataset.value)
    const gst_type = document.getElementById(`product-gst-type-${keys[i]}`).dataset.value

    total_bv += items[keys[i]] * bv
    total_mrp += items[keys[i]] * mrp
    total_dp += ((items[keys[i]] * dp) + ((gst_type === 'EXC') ? ((items[keys[i]] * dp * rate) / 100) : 0))
    total_items += items[keys[i]]
    total_gst += (gst_type === 'EXC') ? ((items[keys[i]] * dp * rate) / 100) : get_gst_value(dp, rate, items[keys[i]])
  }
  console.log(total_gst);
  console.log(items);
  document.getElementById('total-bv').textContent = total_bv
  document.getElementById('total-mrp').textContent = total_mrp
  document.getElementById('total-dp').textContent = total_dp
  document.getElementById('total-amount').textContent = `Amount : ${total_dp}`
  document.getElementById('total-items').textContent = total_items
  document.getElementById('total-gst').textContent = total_gst.toFixed(2)

}

function checkProduct(that) {
  console.log(that.value);
  // const selected_product = ''
  if (that.value) {
    const blocks = document.getElementsByClassName('quantity-block')
    for (let i = 0; i < blocks.length; i++) {
      blocks[i].classList.add('d-none')
    }
    document.getElementById(`quantity-block-${that.value}`).classList.remove('d-none')
  }

}

// mId = document.getElementById('franchise-id').value
async function validatefranchiseIdUsingFetch() {
  const franchise_id = document.getElementById('franchise-id').value.trim()
  const franchise_name = document.getElementById('franchise-name')
  const franchise_mobile_no = document.getElementById('franchise-mobile-no')

  const response = await fetch('/main/get_franchise_details/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `franchise_id=${franchise_id}`, // body data type must match "Content-Type" header
  })
    .then(response => {
      if (response.ok) {
        return response.json()
      } else {
        throw new Error('Network response was not ok.')
      }
    })
    .then(data => {
      if (data.name) {
        franchise_name.value = data.name
        franchise_mobile_no.value = data.mobile_no
        document.getElementById('franchise-id').disabled = true
        document.getElementById('check-id-btn').classList.add('d-none')
        document.getElementById("hidden-field-2").classList.remove('d-none')
        document.getElementById("hidden-field-3").classList.remove('d-none')
        document.getElementById("hidden-field-4").classList.remove('d-none')
        document.getElementById("hidden-field-5").classList.remove('d-none')
        document.getElementById("hidden-field-5").classList.remove('d-none')
      }
      else {
        showWarningToast('Invalid Franchise ID')
      }
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error)

    })

}



function saveBill() {
  // access form elements
  console.log('bill saved');
  const id = document.getElementById('franchise-id').value
  const total_items = document.getElementById('total-items').textContent
  const total_dp = document.getElementById('total-dp').textContent
  const total_bv = document.getElementById('total-bv').textContent
  const total_gst = document.getElementById('total-gst').textContent
  const total_mrp = document.getElementById('total-mrp').textContent

  data = {
    'franchise-id': id,
    'total-items': total_items,
    'total-dp': total_dp,
    'total-bv': total_bv,
    'total-gst': total_gst,
    'total-mrp': total_mrp,
    'items': items,
  }
  url = `/company_admin/saveBill/`
  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data),
  })
    .then(response => response.json())
    .then(data => {
      console.log(data)
      if (data.success)
        // window.location = `/company_admin/bill/view/${data.invoice_id}`;
        document.getElementById('sale-invoices-link').click()

      else
        showDangerToast(data.error)
    })
    .catch(error => console.log('Error', error))


}




async function checkFranchiseId() {
  const franchise_id = document.getElementById('franchise-id').value.trim()
  const valid_franchise_id = await validatefranchiseIdUsingFetch(franchise_id)
  if (document.getElementById('franchise-id').value && valid_franchise_id) {
    document.getElementById('franchise-id').disabled = true
    document.getElementById('check-id-btn').classList.add('d-none')
    document.getElementById("hidden-field-2").classList.remove('d-none')
    document.getElementById("hidden-field-3").classList.remove('d-none')
    document.getElementById("hidden-field-4").classList.remove('d-none')
    document.getElementById("hidden-field-5").classList.remove('d-none')
    document.getElementById("hidden-field-5").classList.remove('d-none')
  }

}