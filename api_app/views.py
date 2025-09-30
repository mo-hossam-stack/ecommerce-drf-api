from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Cart, CartItem, Product,Category
from .serializers import CartSerializer, ProductListSerializer,ProductDetailSerializer,CategoryListSerializer,CategoryDetailSerializer

@api_view(['GET'])
def product_list(request):
    products = Product.objects.filter(featured=True)
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    serializer = ProductDetailSerializer(product)
    return Response(serializer.data)

@api_view(["GET"])
def category_list(request):
    categories = Category.objects.all()
    serializer = CategoryListSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    serializer = CategoryDetailSerializer(category)
    return Response(serializer.data)

@api_view(["POST"])
def add_to_cart(request):
    cart_code = request.data.get("cart_code")
    product_id = request.data.get("product_id")

    cart, created = Cart.objects.get_or_create(cart_code=cart_code)
    product = Product.objects.get(id=product_id)

    cartitem, created = CartItem.objects.get_or_create(product=product, cart=cart)
    cartitem.quantity = 1 
    cartitem.save() 

    serializer = CartSerializer(cart)
    return Response(serializer.data)

@api_view(["PUT"])
def update_cartitem_quantity(request):
    cartitem_id = request.query_params.get("cartitem_id")
    quantity = request.query_params.get("quantity")

    if not cartitem_id or not quantity:
        return Response({"error": "cartitem_id and quantity are required"}, status=status.HTTP_400_BAD_REQUEST)

    cartitem = get_object_or_404(CartItem, id=cartitem_id)

    try:
        quantity = int(quantity)
    except ValueError:
        return Response({"error": "Quantity must be an integer"}, status=status.HTTP_400_BAD_REQUEST)

    if quantity <= 0:
        return Response({"error": "Quantity must be greater than 0"}, status=status.HTTP_400_BAD_REQUEST)

    cartitem.quantity = quantity
    cartitem.save()

    return Response({"message": "Cart item updated successfully", "cartitem_id": cartitem.id, "quantity": cartitem.quantity}, status=status.HTTP_200_OK)
