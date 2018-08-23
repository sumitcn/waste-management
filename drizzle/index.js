$(document).ready(function(){

   let clickCount = 0;
   let clickCount1 = 0;
  $('#username').hide();
 $('#login').click(function(){
   clickCount= clickCount+1;
   if ( clickCount%2 === 1) {
     $('#searchBar').hide();
     $('#registerUser').show();
     // $('#username').show();

   }
   else {
     $('#searchBar').show();
     $('#registerUser').hide();
     // $('#username').hide();
   }
 });
  // $('#register').click(function(){
  //   clickCount1= clickCount1+1;
  //   if ( clickCount1%2 === 1) {
  //     $('.skewedUp,.skewedDown,.upExp,.downExp,footer').addClass("bluredBody");
  //   }
  //   else {
  //     $('.skewedUp,.skewedDown,.upExp,.downExp,footer').removeClass("bluredBody");
  //   }
  // });
 $('#register-page').click(function(){
   $(this).attr("href","register.html");
 });
 $('#fbid').hover(function(){
   $(this).addClass("")
 });
 $('#gid').hover(function(){
   $(this).addClass("")
 });
 $('#twid').hover(function(){
   $(this).addClass("")
 });
 $('#gtid').hover(function(){
   $(this).addClass("")
 });
});
