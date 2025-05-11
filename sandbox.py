#todo: when user input for BookGenre, BookFormat & Language -> options must be displayed, grab user selection and do
# a comparison. They can be added as direct values.

print(book1.get_title())
print(book1)
book1.set_author("new guy")
book1.set_language(Language.FRENCH)
print(book1)
Language.show_available()
BookFormat.show_available()
BookGenre.show_available()
book1.set_language(Language.PORTUGUESE)
print(book1)
order1 = Order("SKU01", "May 10th", OrderStatus.DELIVERED, "monique.dubois@outlook.fr")
order2 = Order("SKU02", "May 9th", OrderStatus.DELIVERED, "monique.dubois@outlook.fr")
order3 = Order("SKU02", "May 9th", OrderStatus.SHIPPED, "monique.dubois@outlook.fr")
order4 = Order("SKU02", "May 9th", OrderStatus.DISPATCHED, "monique.dubois@outlook.fr")
print(order1)
order1.add_book_to_order(book1)
order1.add_book_to_order(book2)
order1.display_order_items()
order1.get_total_amount()
order1.get_total_items()
order1.remove_book_from_order(book2)
order1.get_total_amount()
order1.get_total_items()
order1.set_order_status(OrderStatus.PLACED)
print(order1)


choice = input("")
    if choice == "1":
        choice = book1
    book_list.add_book(choice)
    book_list.updateMinus1_book_list()