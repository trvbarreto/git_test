const container = document.querySelector('#container');

const content = document.createElement('div');
content.classList.add('content');
content.textContent = 'This is the glorious text-content!';

const paragraph1 = document.createElement('p');
paragraph1.style.color = 'red';
paragraph1.textContent = 'Hey I\'m red!';

const heading3 = document.createElement('h3');
heading3.style.color = 'blue';
heading3.textContent = 'I\'m a blue h3';

const div = document.createElement('div');
div.style.border = '1px solid black';
div.style.backgroundColor = 'pink';

const heading1 = document.createElement('h1');
heading1.textContent = 'I\'m in a div';

const paragraph2 = document.createElement('p');
paragraph2.textContent = 'ME TOO!';

div.appendChild(heading1);
div.appendChild(paragraph2);

container.appendChild(content);
container.appendChild(paragraph1);
container.appendChild(heading3);
container.appendChild(div);