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
let edit = {
  isEdit: false,
  index: null,
};

function deleteCard(index) {
  const cardList = JSON.parse(localStorage.getItem("array"));
  const filteredCardList = cardList.filter((_, i) => i !== index);
  localStorage.setItem("array", JSON.stringify(filteredCardList));
  render(foodCardLists);
}

function editCard(index) {
  const data = JSON.parse(localStorage.getItem("array"))[index];
  type.value = data.type;
  title.value = data.title;
  description.value = data.description;
  avatarLink.value = data.avatar;
  imageLink.value = data.image;
  avatarName.value = data.author;
  createdAt.value = data.createdAt;
  edit.isEdit = true;
  edit.index = index;
}

window.deleteCard = deleteCard;
window.editCard = editCard;

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
             <button type="button" class="edit-btn" data-bs-toggle="modal" data-bs-target="#exampleModal"
            data-bs-whatever="@mdo" onclick='editCard(${index})'>Edit</button>
            <button class="delete-btn" onclick='deleteCard(${index})'>Delete</button>
            </section>
        </section>`;
}

function submit() {
  const data = {
    id: Date.now(),
    type: type.value,
    title: title.value,
    description: description.value,
    avatar: avatarLink.value,
    image: imageLink.value,
    author: avatarName.value,
    createdAt: createdAt.value,
  };

  if (JSON.parse(localStorage.getItem("array"))) {
    if (edit && edit.isEdit) {
      edit.isEdit = false;
      const cardList = JSON.parse(localStorage.getItem("array"));
      cardList[edit.index] = data;
      localStorage.setItem("array", JSON.stringify(cardList));
    } else {
      localStorage.setItem(
        "array",
        JSON.stringify([...JSON.parse(localStorage.getItem("array")), data])
      );
    }
  } else {
    localStorage.setItem("array", JSON.stringify([data]));
  }

  render(foodCardLists);
}

submitBtn.addEventListener("click", submit);

function render(array) {
  array.innerHTML = JSON.parse(localStorage.getItem("array"))
    .map(CardItem)
    .join("");
}

render(foodCardLists);
