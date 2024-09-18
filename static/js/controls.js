function handleToggle(item, controls, sections) {
  controls.forEach(control => {
    item != control ? control.children[0].classList.remove('active') : control.children[0].classList.add('active')
  })
  sections.forEach(section => {
    item.dataset.id == section.id ? section.classList.add('d-block') : section.classList.remove('d-block')
  })
}

function submitProfilePhoto() {
  // console.log(document.querySelector('#profile_photo_field').files)
  let formData = new FormData();
  const new_image = document.querySelector('#profile_photo_field').files[0]
  formData.append('profile_photo', new_image);

  fetch('/change_profile_photo/', {
    method: 'POST',
    body: formData,
    headers: {

    }
  }).then(res => res.json())
  .then(data => {
    if (data.success) {
      document.getElementById('profile_image').src = URL.createObjectURL(new_image);
      document.getElementById('nav_profile_image').src = URL.createObjectURL(new_image);
      console.log('Profile photo changed successfully');
    } else {
      console.error('Error changing profile photo:', data.error);
    }
  })
  .catch(error => console.error('Fetch error:', error));

}


function bindEventListeners() {
  document.querySelector('#profile_photo_field').onchange = submitProfilePhoto
  const controls = Array.from(document.querySelector('#control-list').children)
  const sections = Array.from(document.querySelector('#sections').children)
  controls.forEach(item => {
    item.addEventListener('click', () => handleToggle(item, controls, sections))
  });
}

bindEventListeners()









