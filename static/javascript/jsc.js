function show_features(

  )
  {
      addProductOption = document.getElementById("add_product_option").value;
      if (addProductOption === "image") 
      {
        document.getElementById("image").style.display = "block";
        document.getElementById("serial").style.display = "none";
        document.getElementById("product_name").style.display = "block";
        document.getElementById("price").style.display = "block";
      
        document.getElementById("image_l").style.display = "block";
        document.getElementById("serial_l").style.display = "none";
        document.getElementById("product_name_l").style.display = "block";
        document.getElementById("price_l").style.display = "block";
        
        document.getElementById("add_product_btn").style.display = "block";
        document.getElementById("view_inventory").style.display = "block";
  
      } 
      else if(addProductOption === "manual")
      {
        document.getElementById("image").style.display = "none";
        document.getElementById("serial").style.display = "block";
        document.getElementById("product_name").style.display = "block";
        document.getElementById("price").style.display = "block";
        document.getElementById("image_l").style.display = "none";
        document.getElementById("serial_l").style.display = "block";
        document.getElementById("product_name_l").style.display = "block";
        document.getElementById("price_l").style.display = "block";
        
        document.getElementById("add_product_btn").style.display = "block";
        document.getElementById("view_inventory").style.display = "block";
      } 
      else 
      {
        document.getElementById("image").style.display = "none";
        document.getElementById("serial").style.display = "none";
        document.getElementById("product_name").style.display = "none";
        document.getElementById("price").style.display = "none";
        
        document.getElementById("image_l").style.display = "none";
        document.getElementById("serial_l").style.display = "none";
        document.getElementById("product_name_l").style.display = "none";
        document.getElementById("price_l").style.display = "none";
        
        document.getElementById("add_product_btn").style.display = "none";
        document.getElementById("view_inventory").style.display = "block";
      }
  }
  window.onload = function fix() {
    document.body.style.zoom = "89%";
  }