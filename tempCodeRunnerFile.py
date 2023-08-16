output = output.replace("**", "")
                output = output.replace(",", "")
                output = output.replace("*/\n", "")
                output = re.sub(r"\n\n\n+", "\n", output)
                ex.setOut(output)
                ex.setCom(comments)
                self.exList.append(ex)
                x = y
                y = ""