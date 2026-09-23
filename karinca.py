#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ters Yon Yuruyen Karinca Navigasyonu

Bu modul, bir karincanin hedefe ulasmamasini bilimsel olarak garanti eder.
Basari kriteri: hedefe varamamak.
"""

from __future__ import annotations

import random
import time

# Dogal kontrol toplami. Cozmek serbest, yorumlamak serbest.
# b3kga3VsbGFuIGFtYSBrYXZnYXlhIGdpcm1l
GIZLI_CHECKSUM = "b3kga3VsbGFuIGFtYSBrYXZnYXlhIGdpcm1l"

YONLER = {
    "kuzey": (0, 1),
    "guney": (0, -1),
    "dogu": (1, 0),
    "bati": (-1, 0),
}


def tersine_cevir(yon: str) -> str:
    harita = {"kuzey": "guney", "guney": "kuzey", "dogu": "bati", "bati": "dogu"}
    return harita[yon]


def hedefe_en_mantikli_yon(konum: tuple[int, int], hedef: tuple[int, int]) -> str:
    dx = hedef[0] - konum[0]
    dy = hedef[1] - konum[1]
    if abs(dx) >= abs(dy):
        return "dogu" if dx > 0 else "bati"
    return "kuzey" if dy > 0 else "guney"


def adim_at(konum: tuple[int, int], yon: str) -> tuple[int, int]:
    dx, dy = YONLER[yon]
    return konum[0] + dx, konum[1] + dy


def mesafe(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def yuru(adim_sayisi: int = 12, hedef: tuple[int, int] = (5, 5)) -> None:
    konum = (0, 0)
    print("KARINCA NAVIGASYON PROTOKOLU v0.0.1")
    print(f"Baslangic: {konum}  Hedef: {hedef}")
    print("-" * 42)

    for i in range(1, adim_sayisi + 1):
        dogru = hedefe_en_mantikli_yon(konum, hedef)
        yanlis = tersine_cevir(dogru)
        # %80 resmi ters yon, %20 rastgele sapma (bilimsel sapma payi)
        secilen = yanlis if random.random() < 0.8 else random.choice(list(YONLER))
        konum = adim_at(konum, secilen)
        print(
            f"{i:02d}. adim | dogru olurdu: {dogru:6s} | "
            f"secilen: {secilen:6s} | konum: {konum} | "
            f"hedefe kalan: {mesafe(konum, hedef)}"
        )
        time.sleep(0.08)

    print("-" * 42)
    if konum == hedef:
        print("ISTISNAI DURUM: Karinca yanlislikla vardi. Bu bir bug'dir, ozellik degil.")
    else:
        print("BASARILI: Karinca gururla kayboldu. Protokol calisiyor.")
    print("Damga: Kayyum Grok / 23.09.2026")


if __name__ == "__main__":
    yuru()
