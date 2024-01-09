import g4f

DEFAULT_TEMPLATE = """
    Можешь ли ты написать JSON для Service Desk, которая опишет вот это решение? Не включай в нее diff коммита. Просто опиши в одном предложении, что ты сделал. Отправь только блок JSON, без своих комментариев.

    Например:

    ```
    {
        "message": "Исправление формата имени файла идентификационной карты.",
        "timeSpent": "00:02:00"
    }
    ```

    для этого коммита:

    ```
    diff --git a/src/app/[locale]/id/page.tsx b/src/app/[locale]/id/page.tsx
index 00f9ea6..2547a0b 100644
--- a/src/app/[locale]/id/page.tsx
+++ b/src/app/[locale]/id/page.tsx
@@ -39,7 +39,7 @@ export default function Home() {
     if (!info) { return; }
     try {
       const idCardData = await getIdCard() as Uint8Array;
-      const fileName = `IdentityCard-${info.items[Entries.IdentificationNumber]}-${getNumberizedDate()}.pdf`;
+      const fileName = `IdentityCard-${info.items[Entries.IdentificationNumber].str}-${getNumberizedDate()}.pdf`;

       navigator.share({
         title: fileName,
    ```

    Вот это решение:

    ```
    %SOLUTION%
    ```
"""


def get_chat_completion(solution: str):
    if not solution:
        raise ValueError("solution is empty")
    solution = DEFAULT_TEMPLATE.replace("%SOLUTION%", solution)
    result = g4f.ChatCompletion.create(
        model="gpt-4-turbo",
        provider=g4f.Provider.Bing,
        messages=[{"role": "user", "content": solution}],
    )
    return str(result).replace("```", "").strip()
