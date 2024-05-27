document.addEventListener('DOMContentLoaded', function () {
  // Use buttons to toggle between views
  document
    .querySelector('#inbox')
    .addEventListener('click', () => load_mailbox('inbox'));
  document
    .querySelector('#sent')
    .addEventListener('click', () => load_mailbox('sent'));
  document
    .querySelector('#archived')
    .addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = '';
  document.querySelector('#compose-view').style.display = 'none';

  fetch(`/emails/${mailbox}`)
    .then((response) => response.json())
    .then((emails) => {
      // Print emails
      console.log(emails);

      // Get the emails table element
      const emailsTable = document.querySelector('#emails-table');
      // Clear any existing content in the emails table
      emailsTable.innerHTML = `<h3 class='mb-3 ms-1'>${
        mailbox.charAt(0).toUpperCase() + mailbox.slice(1)
      }</h3>`;

      // ... do something else with emails ...
      emails.forEach((element) => {
        // Create a list item for each email
        const li = document.createElement('li');
        // change backround based on if email was read
        if (element.read == true) {
          li.className = 'list-group-item shadow-sm rounded single-email mb-3';
        } else {
          li.className =
            'list-group-item shadow-sm rounded single-email mb-3 active';
        }

        li.innerHTML = `<div class="row">
                            <div class="col-sm-6">
                                <div>
                                    <p class="mb-1 text-singleline text-dark">${element.sender}</p>
                                    <p class="text-muted mb-0 text-singleline">${element.subject}</p>
                                </div>
                            </div>
                            <div class="col-sm-6">
                                <div class="icons">
                                    <p class="mb-1 text-muted">${element.timestamp}</p>
                                    <a class="nav-link mb-0 text-singleline">
                                        <i class="fa-solid fa-box-archive"></i>
                                    </a>
                                </div>
                            </div>
                        </div>`;

        // Add event listener to the email item
        li.addEventListener('click', () => {
          // Remove 'active' class from all items
          document.querySelectorAll('li').forEach((item) => {
            item.classList.remove('active');
          });

          document.querySelector('#email-content').innerHTML = `
                        <div class="p-4">
                            <div class="btn-toolbar mb-3 d-flex justify-content-between"
                                role="toolbar"
                                aria-label="Toolbar with button groups">
                                <div class="btn-group me-2" role="group" aria-label="First group">
                                    <button type="button" class="btn text-muted">
                                        <i class="fa-solid fa-reply"></i>
                                    </button>
                                    <button type="button" class="btn text-muted">
                                      <i class="fa-solid fa-box-archive"></i>
                                    </button>
                                </div>
                            </div>
                            <p class="text-muted mb-1">${element.timestamp}</p>
                            <h5 class="mb-3">${element.subject}</h5>
                            <div>
                                <p class="mb-0">
                                    <span class="text-muted">From :</span> ${element.sender}
                                </p>
                                <p>
                                    <span class="text-muted">To :</span> ${element.recipients}
                                </p>
                            </div>
                            <div>
                                ${element.body}
                            </div>
                        </div>`;

          // Add classname to make visible
          li.classList.add('active');

          // If mail is not read. mark it as read
          if (element.read == false) {
            element.read = true;
            fetch(`/emails/${element.id}`, {
              method: 'PUT',
              body: JSON.stringify({
                read: true,
              }),
            });
          }
        });

        // Append the list item to the emails table
        emailsTable.appendChild(li);
      });
    });
}

addEventListener('DOMContentLoaded', () => {
  document.querySelector('#compose-form').onsubmit = function () {
    console.log('submitted');
    submittedRecipients = document.querySelector('#compose-recipients').value;
    submittedSubject = document.querySelector('#compose-subject').value;
    submittedBody = document.querySelector('#compose-body').value;
    fetch('/emails', {
      method: 'POST',
      body: JSON.stringify({
        recipients: submittedRecipients,
        subject: submittedSubject,
        body: submittedBody,
      }),
    })
      .then((response) => response.json())
      .then((result) => {
        // Print result
        console.log(result);
        load_mailbox('sent');
        document.querySelector('#email-content').innerHTML = 'hi';
      });

    return false;
  };
});
