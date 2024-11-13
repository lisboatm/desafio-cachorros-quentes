def main():
    H, P = map(int, input().split())
    # Calcula a média de cachorros-quentes consumidos por participante
    media = H / P
    # Exibe o resultado com exatamente duas casas decimais
    print(f"{media:.2f}")

if __name__ == "__main__":
    main()
