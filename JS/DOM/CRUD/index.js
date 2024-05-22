const doc = document;
const type = doc.querySelector("form input[id='type']");
const title = doc.querySelector("form input[id='title']");
const imageLink = doc.querySelector("form input[id='imageLink']");
const description = doc.querySelector("form textarea[id='description']");
const avatarLink = doc.querySelector("form input[id='avatarLink']");
const avatarName = doc.querySelector("form input[id='avatarName']");
const createdAt = doc.querySelector("form input[id='createdAt']");
const submitBtn = doc.querySelector(".submit-btn");
const closeBtn = doc.querySelector(".close-btn");
const foodCardLists = doc.querySelector(".food-recipe");
const deleteBtn = doc.querySelector(".card-item  .delete-btn");

function deleteCard(index) {
  const cardList = JSON.parse(localStorage.getItem("array"));
  const filteredCardList = cardList.filter((_, i) => i !== index);
  localStorage.setItem("array", JSON.stringify(filteredCardList));
  render(foodCardLists);
}

window.deleteCard = deleteCard;

function CardItem(data, index) {
  const { title, type, description, author, avatar, image, createdAt } = data;
  return `<section class="card-item">
            <img class="image" src="${image}" width="100%" alt="img">
            <article class="content">
                <p class="title">${type}</p>
                <p>${title}${index}</p>
                <p class="description">${description}</p>
                <article class="profile">
                    <img src="${avatar}"
                        alt="img" width="100%" class="avatar">
                    <div class="details">
                        <p class="title">${author}</p>
                        <p class="subtitle">${createdAt}</p>
                    </div>
                </article>
            </article>
            <section class='btns'>
            <button class="edit-btn">Edit</button>
            <button class="delete-btn" onclick='deleteCard(${index})'>Delete</button>
            </section>
        </section>`;
}

submitBtn.addEventListener("click", function () {
  const data = {
    type: type.value,
    title: title.value,
    description: description.value,
    avatar: avatarLink.value,
    image: imageLink.value,
    author: avatarName.value,
    createdAt: createdAt.value,
  };

  if (JSON.parse(localStorage.getItem("array"))) {
    localStorage.setItem(
      "array",
      JSON.stringify([...JSON.parse(localStorage.getItem("array")), data])
    );
  } else {
    localStorage.setItem("array", JSON.stringify([data]));
  }

  render(foodCardLists);
});

function render(array) {
  array.innerHTML = JSON.parse(localStorage.getItem("array"))
    .map(CardItem)
    .join("");
}

render(foodCardLists);

// deleteBtn.addEventListener("click", function () {});
