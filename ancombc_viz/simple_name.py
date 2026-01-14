def extract_p_g_or_f(top: str) -> str:
    """
    formatting taxon string return to level(p/f/g).
    """
    if top == "Others":
        return "Others"

    parts = top.split(";")
    p = [x for x in parts if x.startswith("p__")]
    c = [x for x in parts if x.startswith("c__")]
    o = [x for x in parts if x.startswith("o__")]
    f = [x for x in parts if x.startswith("f__")]
    g = [x for x in parts if x.startswith("g__")]

    stripped = top.strip()
    last = parts[-1]
    # 0) 완전히 "o__;f__;g__" 패턴으로 끝나는 경우 → p + c
    if len(parts) >= 3 and parts[-3:] == ["o__", "f__", "g__"]:
        pg = ";".join(p + c)

    # 1) "g__"로 끝나지만 genus 이름이 비어 있는 경우 → p + f
    elif last == "g__":
        pg = ";".join(p + f)

    # 2) g__ 이름이 있고, 그걸로 끝나는 경우 → p + g (정상적인 genus)
    elif g and stripped.endswith(g[-1]):
        pg = ";".join(p + g)

    # 3) g__는 없고 f__로 끝나는 경우 → p + c
    elif (not g) and f and last.startswith("f__"):
        pg = ";".join(p + c)

    # 기본: p + g (g가 없으면 p만)
    else:
        pg = ";".join(p + g)

    return pg if pg else top