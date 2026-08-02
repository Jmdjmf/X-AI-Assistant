def calculate(text):
    try:
        text = text.lower()

        if "calculate" not in text and "what is" not in text:
            return None

        expression = (
            text.replace("calculate", "")
                .replace("what is", "")
                .strip()
        )

        result = eval(expression)

        return f"The answer is {result}, Sir."

    except:
        return None
