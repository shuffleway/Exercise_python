const BASE_URL = "http://localhost:5000/api";

/** Generate HTML for a single cupcake item */
function generateCupcakeHTML(cupcake) {
  return `
    <li data-cupcake-id="${cupcake.id}">
     <img class="Cupcake-img" src="${cupcake.image}" alt="${cupcake.flavor}">
      <div class="cupcake-info">
        <p>${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}</p>
      </div>    
      <button class="delete-button">X</button>
      <button class="edit-button">Edit</button>
    </li>
  `;
}

/** Display initial cupcakes on page */
async function showInitialCupcakes() {
  const response = await axios.get(`${BASE_URL}/cupcakes`);
  $("#cupcakes-list").empty();

  for (let cupcakeData of response.data.cupcakes) {
    let newCupcake = $(generateCupcakeHTML(cupcakeData));
    $("#cupcakes-list").append(newCupcake);
  }
}

/** Handle clicking edit button to populate form with cupcake data */
$("#cupcakes-list").on("click", ".edit-button", function (evt) {
  evt.preventDefault();

  const $cupcake = $(evt.target).closest("li");
  const cupcakeId = $cupcake.attr("data-cupcake-id");

  const flavor = $cupcake.find(".cupcake-info p").text().split(" / ")[0];
  const size = $cupcake.find(".cupcake-info p").text().split(" / ")[1];
  const rating = $cupcake.find(".cupcake-info p").text().split(" / ")[2];
  const image = $cupcake.find("img").attr("src");

  // Set form fields with existing cupcake data for editing
  $("#cupcake-id").val(cupcakeId); // Set the hidden input with cupcake ID

  console.log("After setting, hidden #cupcake-id value is:", $("#cupcake-id").val()); // Debug line

  $("#form-flavor").val(flavor);
  $("#form-size").val(size);
  $("#form-rating").val(rating);
  $("#form-image").val(image);

  // Update the form button text to indicate edit mode
  $("#new-cupcake-form button[type='submit']").text("Update Cupcake");
});

/** Handle form submission for adding or editing a cupcake */
$("#new-cupcake-form").on("submit", async function (evt) {
  evt.preventDefault();

  const cupcakeId = $("#cupcake-id").val(); // Check if we're in edit mode

  const flavor = $("#form-flavor").val();
  const rating = $("#form-rating").val();
  const size = $("#form-size").val();
  const image = $("#form-image").val() || null;

  if (cupcakeId) {
    try {
      const response = await axios.patch(`${BASE_URL}/cupcakes/${cupcakeId}`, {
        flavor,
        rating,
        size,
        image
      });
      const updatedCupcakeHTML = generateCupcakeHTML(response.data.cupcake);
      $(`[data-cupcake-id="${cupcakeId}"]`).replaceWith(updatedCupcakeHTML);
    } catch (err) {
      console.error("Failed to update cupcake:", err);
    }
  } else {
    try {
      const response = await axios.post(`${BASE_URL}/cupcakes`, {
        flavor,
        rating,
        size,
        image
      });
      const newCupcakeHTML = generateCupcakeHTML(response.data.cupcake);
      $("#cupcakes-list").append(newCupcakeHTML);
    } catch (err) {
      console.error("Failed to add cupcake:", err);
    }
  }

  // Reset the form and switch back to add mode
  $("#new-cupcake-form").trigger("reset");
  $("#cupcake-id").val(""); // Clear cupcake ID to exit edit mode
  $("#new-cupcake-form button[type='submit']").text("Save"); // Reset button text
});



/** Handle clicking delete button to remove cupcake */
$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("li");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  if (cupcakeId) {
    try {
      await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
      $cupcake.remove();
    } catch (err) {
      console.error("Failed to delete cupcake:", err);
    }
  } else {
    console.error("Cupcake ID not found for deletion.");
  }
});

/** Handle clicking edit button to populate form with cupcake data */
$("#cupcakes-list").on("click", ".edit-button", function (evt) {
  evt.preventDefault();

  const $cupcake = $(evt.target).closest("li");
  const cupcakeId = $cupcake.attr("data-cupcake-id");
  const flavor = $cupcake.find(".cupcake-info p").text().split(" / ")[0];
  const size = $cupcake.find(".cupcake-info p").text().split(" / ")[1];
  const rating = $cupcake.find(".cupcake-info p").text().split(" / ")[2];
  const image = $cupcake.find("img").attr("src");

  // Set form fields with existing cupcake data for editing
  $("#cupcake-id").val(cupcakeId); // Set the hidden input with cupcake ID
  $("#form-flavor").val(flavor);
  $("#form-size").val(size);
  $("#form-rating").val(rating);
  $("#form-image").val(image);

  // Update the form button text to indicate edit mode
  $("#new-cupcake-form button[type='submit']").text("Update Cupcake");
});

// Show initial cupcakes when the page loads
$(showInitialCupcakes);