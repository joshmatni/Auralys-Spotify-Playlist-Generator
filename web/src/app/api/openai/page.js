import { OpenAI } from "openai";

const openai = new OpenAI();

//Create a new instance of OpenAIApi with your API key

export default async (req, res) => {
  if (1 == 1) {
    try {
      const completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{ role: "system", content: "You are an assistant skilled in extracting keywords from the prompt for playlist generation and music"},
        {"role": "user", "content": `${req.body.prompt}`}],
      });

      const content = completion.data.choices[0].message.content;

      res.status(200).json({ text: content });
    } catch (error) {
      console.log(error);
    }
  } else {
    res.status(400).json({ text: "No prompt provided." });

  }
};
