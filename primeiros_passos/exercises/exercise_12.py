try:
    app_is_running = True
    market_list = []

    while app_is_running:
        print("=" * 20)
        print("MINHA LISTA DE COMPRAS".center(20))
        print("[A]dicionar")
        print("[E]ditar")
        print("[C]onsultar")
        print("[D]eletar")
        print("[S]air")
        print("=" * 20)
        app_user_command_input = input("Informe a operação >> ")
        app_user_command_formatted_input = app_user_command_input.lower()

        if app_user_command_formatted_input == "a":
            market_product_add_input = input("Informe o novo produto: ")
            in_product_market_list = market_product_add_input in market_list
            if in_product_market_list:
                print("Esse produto já existe")
            if not in_product_market_list:
                market_list.append(market_product_add_input)
                print("Produto cadastrado com sucesso!")
        if app_user_command_formatted_input == "e":
            try:
                market_product_update_input = input("Informe o produto a ser editado: ")
                in_product_market_list = market_product_update_input in market_list
                if in_product_market_list:
                    new_product_name_input = input("Adicione o novo nome: ")
                    market_list_index = market_list.index(market_product_update_input)
                    market_list[market_list_index] = new_product_name_input
                    print("Edição feita com sucesso!")
                if not in_product_market_list:
                    print("Produto não encontrado!")
            except (IndexError, ValueError):
                print("Index inválido!")
        if app_user_command_formatted_input == "c":
            market_list_enum = enumerate(market_list, start=1)
            for market_list_index, market_list_item in market_list_enum:
                print("=" * 20)
                print(f"{market_list_index} - {market_list_item}")
                print("=" * 20)
        if app_user_command_formatted_input == "d":
            try:
                market_product_delete_input = input(
                    "Informe o produto a ser deletado: "
                )
                in_product_market_list = market_product_delete_input in market_list
                if in_product_market_list:
                    market_list_index = market_list.index(market_product_delete_input)
                    del market_list[market_list_index]
                    print("Produto removido com sucesso!")
                if not in_product_market_list:
                    print("Produto não encontrado!")
            except (IndexError, ValueError):
                print("Index inválido!")
        if app_user_command_formatted_input == "s":
            print("=" * 20)
            print("PROGRAMA FINALIZADO".center(20))
            print("=" * 20)
            app_is_running = False
except (KeyboardInterrupt, EOFError):
    print("Fechado pelo usuário")
