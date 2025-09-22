def mo_ta_nam(nam: int) -> str:
    thap_ky = (nam // 10) * 10
    if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
        return f"Năm nhuận của thập kỷ {thap_ky}s"
    else:
        return f"Năm không nhuận của thập kỷ {thap_ky}s"

print(mo_ta_nam(2024))