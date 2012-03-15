$(function () {						
	initialization = function () {
		// set up page
		bindEvents();
		loadData();

		$(window).resize(function () {
		});
	},
	
	bindEvents = function () {
		$('#new-item-form').submit(function (ev){
		  ev.preventDefault();
		  ev.stopPropagation();
		  
		  var
		  input = $('#add-new-item'),
		  amount = parseInt(input.val(), 10);
		  
		  if (amount) {
		    input.removeClass('error');
		    addNewItem(amount, $('#item-title').val());
		  } else {
		    input.addClass('error');
		  }
		  return false;
		});
		
		$('#item-title').keydown(function (ev) {
		  if (ev.keyCode === 13) {
		    $('#new-item-form').submit();
		  }
		});
  },
  
  loadData = function () {
    $.ajax({
      url: 'js/data.json',
      dataType: 'json',
  		type: 'GET',
      success: function (data) {
        render(data);
      },
      error: function() {
        alert('error');
      }
    });
  },
  
  render = function (data) {
    var total = 0;
    
    $.each(data.entries, function (count, entry) {
      total += entry.cost;
      addNewItem(entry.cost, entry.title);
    });
    
    $('#current-total').text('$' + total);
    $('#status-bar-percentage').css('width',  (total / data.budget * 100) + '%');
    $('#monthly-budget').val('$' + data.budget);
  },
  
	addNewItem = function (amount, title) {
    hideZeroState();
    amount = formatAmount(amount);
    
    updateTotal(amount);
    
    var template = $('<li><span class="spent-amount">$'+ amount + '</span><input class="spent-title" value="' + title + '" /></li>');
    $('#default-state').prepend(template);
    resetForm();
  },
  
  updateProgressBar = function (total) {
    var budget = parseInt($('#monthly-budget').val().split('$')[1]),
    percent = (total / budget * 100);
    
    if (percent > 100) {
      $('#status-bar-percentage').animate({
        'width' : '100%'
      });
      
      $('#status-bar').addClass('over');   
    } else {     
      $('#status-bar-percentage').animate({
        'width' : (total / budget * 100) + '%'
      });
    }
  },
  
  updateTotal = function (amount) {
    var total = $('#current-total').text();
    
    total = parseInt(total.split('$')[1]);
    
    total += parseInt(amount);
    $('#current-total').text('$' + total);
    
    updateProgressBar(total);
  },
  
  resetForm = function () {
    $('#add-new-item').val('').focus();
    $('#item-title').val('').blur();
  },
  
  hideZeroState = function () {
    if (!$('#spending-list').hasClass('loading')) {
      return;
    }
    $('#spending-list').removeClass('loading');
  },
  
  formatAmount = function (n) {
    return (n+'').replace(/(^|[^\w.])(\d{4,})/g, function(_, $1, $2) {
      return $1 + $2.replace(/\d(?=(?:\d\d\d)+(?!\d))/g, "$&,");
    });
  }
});

$(document).ready(function (){
	initialization();
});