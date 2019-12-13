//=====Базовые значения=====//
var slots_per_reel = 8; //кол-во ячеек в барабане
//НЕ ЗАБЫВАЙ, ЧТО ИЗНАЧАЛЬНО ПРОПИСАНО 8 ДИВОВ В HTML (а то я тупил так 3 часа в чем же, блять, проблема)

var reels = 3; //кол-во барабанов

var slotAngle = 360 / slots_per_reel; //шаг поворота

//Расчет радиуса(кол-во ячеек)
function getReelRadius(slots_per_reel) {
	let panelHeight = $(ring1).height();
	return Math.round( ( panelHeight / 2) / Math.tan( Math.PI / slots_per_reel ) ); 
}

var reel_radius = getReelRadius(slots_per_reel);

//Запоминаем углы поворота барабанов
var rotateAngle = [];

//Текущий выпавший слот
var currentSlot = [8, 8, 8]

function rotateAngleInit() {
	for(let i = 0; i <reels; i++) {
		rotateAngle[i] = 0;
	}
}

//Рендер барабана(кол-во ячеек)
//передавая ниже в функцию переменную с одинаковым названием, используется уже локальная переменная
//Вообще не знаю зачем в эту функцию что-топ передовать, если они глобальные, но мне нравится оранжевый
function RenderSlots(reels, slots_per_reel, slotAngle) {
	let panelHeight = $(ring1).height();
	console.log("==========RenderSlots Debug============");
	for (let j = 1; j <= reels; j++) {
		for (let i = 1; i <= slots_per_reel; i++) {
			let transform = 'rotateX(' + (slotAngle * i) + 'deg) translateZ(' + reel_radius + 'px)';
			console.log(transform);
			$('#' + j + '-' + i).css('transform', transform);
		}
	}
	console.log("=======================================");
}

//Добавление барабана
function AddReel() {
	reels++;

	//Создание контейнера под ring и кнопки
	let t_container = document.createElement('div');
	t_container.id = "container" + reels;
	t_container.className = "buttons-container";
	$('#reelsContainer').append(t_container);

	//Создание контейнера под слоты
	let t_ring = document.createElement('div');
	t_ring.id = "ring" + reels;
	t_ring.className = "ring";
	// let panelHeight = $(ring1).height();
	// t_ring.style.padding = "0px 0px " + panelHeight + "px";
	/*t_ring.attr('id', 'ring' + reels);*/
	$('#container' + reels).append(t_ring);

	//Создание кнопок
	let t_button = document.createElement('div');
	t_button.id = "cp" + reels;
	t_button.className = "control-panel";
	//Я попаду в ад за строчку ниже
	t_button.innerHTML = "<div id='cp" + reels + "' class='control-panel'><button class='GoSpinSlot'>Spin Slot</button><button class='GoSpinReel'>Spin Reel</button><button class='GoEditReel'>Edit Reel</button><button class='GoDelReel'>Del Reel</button></div>"; //Ты ничего не видел
	$('#container' + reels).append(t_button);

	//Создание ячеек
	for (let i = 1; i <= slots_per_reel; i++) {
		let slot = document.createElement('div');
		slot.className = "slot";
		/*slot.attr('id', reels + '-' + i)*/
		slot.id = reels + '-' + i;
		$('#ring' + reels).append(slot);
		$(slot).append('Test');
		let transform = 'rotateX(' + (slotAngle * i) + 'deg) translateZ(' + reel_radius + 'px)';
		$('#' + reels + '-' + i).css('transform', transform);
	}

	//Добавляем счетчик угла поворота на новый барабан
	rotateAngle[reels - 1] = 0;

	//Запоминаем текущий выпавший слот (по дефолту 8-й)
	currentSlot[reels - 1] = 8;
}

//Удаление барабана
function DelReel(elem) {
	$(elem).closest('.buttons-container').remove();
	//Добавить переписывание ID последующих блоков и обновление инфы в массивах
}

function EditReel(elem) {
	let currentId = elem.closest('.control-panel').id[2]; 
	for (let i = 1; i <= slots_per_reel; i++) {
		$('#' + currentId + '-' + i).attr('contenteditable', 'true');
	}
}


//========================Прокрутка=================================//

//Прокрутка барабана на 1 слот slotAngle * 1 ()
function SlotSpin(elem) {
	let currentId = elem.closest('.control-panel').id[2]; 
	//вынести поиск в отдельную функцию, чтобы можно было передать любой элемент
	//И переписать всю прокрутку, чтобы убрать костыли
	//Поиск должен считывать нужное кол-во цифр в зависимости от id.Length(). Сейчас читает одну
	currentId = Number(currentId);
	rotateAngle[currentId - 1] -= slotAngle; 

	//Почему вообще я обозначил слоты с единицы. А теперь лень переписывать
	let transform = 'rotateX(' + rotateAngle[currentId - 1] + 'deg)';
	$('#ring' + currentId).css('transition', 'transform 2s ease-in-out');
	$('#ring' + currentId).css('transform', transform);
	currentSlot[currentId - 1]++;
	if (currentSlot[currentId - 1] > slots_per_reel) {
		currentSlot[currentId - 1] = 1;
	}
}

//Полная прокрутка барабана slotAngle * slot_per_reels (кол-во раз)
function ReelSpin(elem, count) {
	let myrandom = getRandomInt(1, slots_per_reel);
	for (let i = 0; i < count; i++) { 
		for (let j = 0; j < myrandom; j++) {
			SlotSpin(elem);
		}
	}
}

//Полная прокрутка всех барабанов
function MachineSpin() {
	let min = 1;
	let max = 2;
	let count;
	for (let i = 1; i <= reels; i++) {
		var element = document.querySelectorAll('.GoSpinReel');
		//var element2 = $('#container' + i).find('.GoSpinReel');
		count = getRandomInt(min, max);
		ReelSpin(element[i - 1], count);
		min += count;
		max += count;
	}
}
//==================================================================//


//===========================SERVER=================================//
function ParseIt() {
	let Matrix = [];
	for (let i = 1; i <= reels; i++) {
		let currentArray = []; //Если вынести за for(i), то ссылки в матрице будут указывать на последний массив
		for (let j = 1; j <= slots_per_reel; j++) {
		currentArray[j - 1] = $('#' + i + '-' + j).html(); 
		}
		Matrix[i - 1] = currentArray;
	}
	return Matrix;
}

//А вот это точно временно, не убивайте. Пусть будет 8 барабанов по 8 слотов и всё будет хорошо
var FirstSave = true;
//Сформируем нужный JSON и отправим
function SaveIt(Matrix) {
	let MyReel = {};
	for (let i = 0; i < reels; i++) {
		    MyReel = {
			reelset: i,
			name: "Забыл добавить названия, точно",
			description: "Куда его на странице влепить?",
			field0: Matrix[i][0],
			field1: Matrix[i][1],
			field2: Matrix[i][2],
			field3: Matrix[i][3],
			field4: Matrix[i][4],
			field5: Matrix[i][5],
			field6: Matrix[i][6],
			field7: Matrix[i][7]
		};
		//Передаём на сервер
		if (FirstSave == true) {
			let username1 = $("input#username").val();
			let password1 = $("input#password").val();
			$.ajax({
				url: 'http://pazhur.herokuapp.com/api/reels/',
				method: 'POST',
				contentType: 'application/json',
				data: JSON.stringify(MyReel),
				beforeSend: function(xhr) {
		 		xhr.setRequestHeader("Authorization", "Basic " + btoa(username1 + ":" + password1));
		 		}
			})
			.done(function() {
				console.log('POST OK');
			})
			.fail(function () {
				console.log('POST NE OK')
			});
			FirstSave = false;
		}
		else {
			$.ajax({
				url: 'http://pazhur.herokuapp.com/api/reels/',
				method: 'PUT',
				contentType: 'application/json',
				data: JSON.stringify(MyReel),
			})
			.done(function() {
				console.log('PUT OK');
			})
			.fail(function () {
				console.log('PUT NE OK')
			});
		}
	}
}

function getDefReelSets() {
	let DefReelSets = $.ajax({
		url: 'http://pazhur.herokuapp.com/api/default_reel_sets/',
		method: 'GET',
		contentType: 'application/json',
	})
	.done(function() {
		console.log('GET OK');
	})
	.fail(function() {
		console.log('GET NE OK')
	});
	return typeof DefReelSets === "string" ? JSON.parse(DefReelSets) : DefReelSets;
}

function getReelSet(count) {
	let ReelSet = $.ajax({
		url: 'http://pazhur.herokuapp.com/api/default_reel_sets/' + count + '/',
		method: 'GET',
		async: false,
		contentType: 'application/json'
		// success: function () {
		// 	data = JSON.parse(data);
		// }
	})
	.done(function() {
		console.log('GET DEFAULT REEL SETS OK');
	})
	.fail(function() {
		console.log('GET DEFAULT REEL SETS NE OK')
	});
	typeof ReelSet === "string" ? JSON.parse(ReelSet) : ReelSet;
	let IDs = [];
	let reels1 = {};
	for (let i = 0; i < 8; i++) {
		IDs[i] = ReelSet.responseJSON.reels[i];
	}
	return IDs;
}

function UnparseIt(IDs) {
	let Temp = [];
	let Matrix = [];
	for (let i = 0; i < 8; i++) {
			Temp = $.ajax({
			url: 'http://pazhur.herokuapp.com/api/default_reels/' + IDs[i] + '/',
			method: 'GET',
			async: false,
			contentType: 'application/json'
			// success: function () {
			// 	data = JSON.parse(data);
			// }
		})
		.done(function() {
			console.log('GET REEL SET OK');
		})
		.fail(function() {
			console.log('GET REEL SET NE OK')
		});
		typeof Temp === "string" ? JSON.parse(Temp) : Temp;
		let currentArray = [];
		currentArray[0] = Temp.responseJSON.field0;
		currentArray[1] = Temp.responseJSON.field1;
		currentArray[2] = Temp.responseJSON.field2;
		currentArray[3] = Temp.responseJSON.field3;
		currentArray[4] = Temp.responseJSON.field4;
		currentArray[5] = Temp.responseJSON.field5;
		currentArray[6] = Temp.responseJSON.field6;
		currentArray[7] = Temp.responseJSON.field7;
		Matrix[i] = currentArray;
	}
	return Matrix;
}

function SetValues(Matrix) {	
	for (let i = 1; i <= 8; i++) {
		if (reels < i) {
			AddReel();
		}
		for (let j = 1; j <= 8; j++) {
			$('#' + i + '-' + j).text(Matrix[i - 1][j - 1]);
		}
	}
}



function BaseAuth(user, password) { //Зачем я её писал, если есть btoa()
	let tok = user + ':' + password;
	let hash = Base64.encode(tok);
	return "Basic " + hash;
}

function GoAuth() {
	let username1 = $("input#username").val(); //работает
	let password1 = $("input#password").val();
	$.ajax({
		type: "GET",
		url: "http://pazhur.herokuapp.com/",
		dataType: 'json',
		//async: false,
		 beforeSend: function(xhr) {
		 xhr.setRequestHeader("Authorization", "Basic " + btoa(username1 + ":" + password1));
		 },
		data: "Authorization: Basic " + btoa(username1 + ':' + password1),
		username: btoa(username1),
		password: btoa(password1),
		success: function() {
			alert('It Works!');
		}
	})
	.done(function() {
		alert('AUTH OK');
	})
	.fail(function() {
		alert('AUTH NE OK');
	});
}


//==================================================================//


//-----------------------Дополнительно------------------------------//
//дайте полноценный генератор уже
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min + 1)) + min; //Максимум и минимум включены
}

function ajaxSetUp() {
	$.ajaxSetup({
		url: "http://pazhur.herokuapp.com/api/"
	});
}
//------------------------------------------------------------------//



//=======================Инициализация==============================//

$(document).ready(function() {
	rotateAngleInit();
	RenderSlots(reels, slots_per_reel, slotAngle);
	ajaxSetUp();
	//Хуки статических элементов

	$('#login').on('click',function() {
		GoAuth();
	})

	$('.GoSpinSlotMachine').on('click',function() {
		MachineSpin();
	})

	$('.GoAddReel').on('click',function() {
		AddReel();
	})

	$('#xray').on('click',function() {
		$('#reelsContainer').toggleClass('perspective');
	})
	$('.GoFirstSet').on('click', function() {
		SetValues(UnparseIt(getReelSet(1)));
	})
	$('.GoSecondSet').on('click', function() {
		SetValues(UnparseIt(getReelSet(3)));
	})

	//Хуки динамических элементов
	$('#reelsContainer').on('click', '.GoSpinSlot', function() {
		SlotSpin(this);
	})
	$('#reelsContainer').on('click', '.GoSpinReel', function() {
		ReelSpin(this, 1);
	})
	$('#reelsContainer').on('click', '.GoDelReel', function() {
		DelReel(this);
	})	
	$('#reelsContainer').on('click', '.GoEditReel', function() {
		EditReel(this);
	})	
});

//==================================================================//