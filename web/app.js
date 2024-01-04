class Chatbox {
  constructor() {
    this.args = {
      openButton: document.querySelector('.chatbox__button'),
      chatBox: document.querySelector('.chatbox__support'),
      sendButton: document.querySelector('.send__button'),
    };

    this.state = false;
    this.messages = [];
  }

  display() {
    const { openButton, chatBox, sendButton } = this.args;

    openButton.addEventListener('click', () => this.toggleState(chatBox));

    sendButton.addEventListener('click', () => this.onSendButton(chatBox));

    const node = chatBox.querySelector('input');
    node.addEventListener('keyup', ({ key }) => {
      if (key === 'Enter') {
        this.onSendButton(chatBox);
      }
    });
  }

  toggleState(chatbox) {
    this.state = !this.state;

    // show or hides the box
    if (this.state) {
      chatbox.classList.add('chatbox--active');
    } else {
      chatbox.classList.remove('chatbox--active');
    }
  }

  onSendButton(chatbox) {
    var textField = chatbox.querySelector('input');
    let text1 = textField.value;
    if (text1 === '') {
      return;
    }

    let msg1 = { name: 'User', message: text1 };
    this.messages.push(msg1);

    fetch('http://127.0.0.1:5000/predict', {
      method: 'POST',
      body: JSON.stringify({ message: text1 }),
      mode: 'cors',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((r) => r.json())
      .then((r) => {
        let msg2 = { name: 'Sam', message: r.answer };
        this.messages.push(msg2);
        this.updateChatText(chatbox);
        textField.value = '';
      })
      .catch((error) => {
        console.error('Error:', error);
        this.updateChatText(chatbox);
        textField.value = '';
      });
  }

  updateChatText(chatbox) {
    var html = '';
    this.messages
      .slice()
      .reverse()
      .forEach(function (item, index) {
        if (item.name === 'Sam') {
          html += '<div class="messages__item messages__item--visitor">' + item.message + '</div>';
        } else {
          html += '<div class="messages__item messages__item--operator">' + item.message + '</div>';
        }
      });

    const chatmessage = chatbox.querySelector('.chatbox__messages');
    chatmessage.innerHTML = html;
    chatmessage.scrollTo(1, -Infinity); //mới thêm zoo
  }
}

const chatbox = new Chatbox();
chatbox.display();


//thay doi ảnh
document.addEventListener("DOMContentLoaded", function() {
  var images = [
    "https://danangbest.com/uploads/banner-danangbest.webp",
    "https://vcdn1-dulich.vnecdn.net/2022/06/03/cauvang-1654247842-9403-1654247849.jpg?w=1200&h=0&q=100&dpr=1&fit=crop&s=Swd6JjpStebEzT6WARcoOA",
    "https://wiki-travel.com.vn/Uploads/picture/Thaophuongnguyen-171621041606-da-1.jpg",
  ];

  var currentIndex = 0;
  var sliderImage = document.querySelector('.slide-show img');

  // Function to change the image
  function changeImage() {
    currentIndex = (currentIndex + 1) % images.length;
    sliderImage.src = images[currentIndex];
  }

  // Set interval to change image every 3 seconds
  setInterval(changeImage, 3000);
});


const datas = [
  {
    id: 1,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn - Hội An ',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 2,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 3,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 4,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 5,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 6,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 7,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 8,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 9,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 10,
    image: 'https://danangbest.com/uploads/product/nui-than-tai1.webp',
    title: 'Núi Thần Tài',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 11,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn-Hội An ',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 12,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 13,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 14,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 15,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 16,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 17,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 18,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 19,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '1 Ngày',
    start: 'Hằng Ngày',
  },
];

const datas2 = [
  {
    id: 1,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn - Hội An ',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 2,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 3,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 4,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 5,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 6,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 7,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 8,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 9,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 10,
    image: 'https://danangbest.com/uploads/product/nui-than-tai1.webp',
    title: 'Núi Thần Tài',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 11,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn-Hội An ',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 12,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 13,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 14,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 15,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 16,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 17,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 18,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 19,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '2 Ngày',
    start: 'Hằng Ngày',
  },
];

const datas3 = [
  {
    id: 1,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn - Hội An ',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 2,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 3,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 4,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 5,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 6,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 7,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 8,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 9,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 10,
    image: 'https://danangbest.com/uploads/product/nui-than-tai1.webp',
    title: 'Núi Thần Tài',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 11,
    image: 'https://danangbest.com/uploads/product/ngu-hanh-son-hoi-an-1-ngay.webp',
    title: 'Ngũ Hành Sơn-Hội An ',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 12,
    image: 'https://danangbest.com/uploads/product/ba-na-hills-2-ngay-1-dem1.webp',
    title: 'Bà Nà - Ngũ Hành Sơn',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 13,
    image: 'https://danangbest.com/uploads/product/nui-than-tai-1-ngay.webp',
    title: 'Núi Thần Tài',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 14,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-hue1.webp',
    title: 'Huế',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 15,
    image: 'https://danangbest.com/uploads/product/rung-dua-bay-mau-hoi-an1.webp',
    title: 'Hội An',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 16,
    image: 'https://danangbest.com/uploads/product/tour-da-nang-lang-khai-dinh-dai-noi.webp',
    title: 'Hà Nội',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 17,
    image: 'https://danangbest.com/uploads/product/thanh-dia-my-son.webp',
    title: 'Thánh Địa Mỹ Sơn',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 18,
    image: 'https://danangbest.com/uploads/product/bao-tang-da-nang1.webp',
    title: 'Bảo Tàn Đà Nẵng',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
  {
    id: 19,
    image: 'https://danangbest.com/uploads/product/cu-lao-cham-di-bo-duoi-bien.webp',
    title: 'Cù Lao Chàm Đi Bộ Dưới Biển',
    time: '3 Ngày',
    start: 'Hằng Ngày',
  },
];

function createProductCards(data) {
  const container = document.getElementById('productContainer');

  data.forEach(item => {
    // Create card element
    const card = document.createElement('div');
    card.classList.add('product-card');

    // Create card content
    card.innerHTML = `
      <div class="card-image">
        <img src="${item.image}" alt="">
      </div>
      <div class="card__info">
        <h3 class="card__title">${item.title}</h3>
        <p class="card__time">Thời Gian: <span>${item.time}</span></p>
        <p class="card__time">Khởi Hành: <span>${item.start}</span></p>
      </div>
      <div class="buttons">
        <button class="card__btn">Liên Hệ</button>
      </div>
    `;

    // Append card to container
    container.appendChild(card);
  });
}



// Call the function with the data
createProductCards(datas);

function createProductCards2(data) {
  const container = document.getElementById('productContainer2');

  data.forEach(item => {
    // Create card element
    const card = document.createElement('div');
    card.classList.add('product-card');

    // Create card content
    card.innerHTML = `
      <div class="card-image">
        <img src="${item.image}" alt="">
      </div>
      <div class="card__info">
        <h3 class="card__title">${item.title}</h3>
        <p class="card__time">Thời Gian: <span>${item.time}</span></p>
        <p class="card__time">Khởi Hành: <span>${item.start}</span></p>
      </div>
      <div class="buttons">
        <button class="card__btn">Liên Hệ</button>
      </div>
    `;

    // Append card to container
    container.appendChild(card);
  });
}


createProductCards2(datas2);

function createProductCards3(data) {
  const container = document.getElementById('productContainer3');

  data.forEach(item => {
    // Create card element
    const card = document.createElement('div');
    card.classList.add('product-card');

    // Create card content
    card.innerHTML = `
      <div class="card-image">
        <img src="${item.image}" alt="">
      </div>
      <div class="card__info">
        <h3 class="card__title">${item.title}</h3>
        <p class="card__time">Thời Gian: <span>${item.time}</span></p>
        <p class="card__time">Khởi Hành: <span>${item.start}</span></p>
      </div>
      <div class="buttons">
        <button class="card__btn">Liên Hệ</button>
      </div>
    `;

    // Append card to container
    container.appendChild(card);
  });
}

createProductCards3(datas3);