import { Configuration, OpenAIApi } from "openai";
const configuration = new Configuration({
  apiKey: process.env.NEXT_PUBLIC_OPENAIKEY,
});
const openai = new OpenAIApi(configuration);

export default async (req, res) => {
  if (1 == 1) {
    try {
      const completion = await openai.createChatCompletion({
        model: "gpt-3.5-turbo",
        messages: [{ role: "user", content: `${req.body.prompt}` }],
      });

      res
        .status(200)
        .json({ text: `${completion.data.choices[0].message.content}` });

      // return completion.data.choices[0].message.content;
    } catch (error) {
      console.log(error);
    }
  } else {
    res.status(400).json({ text: "No prompt provided." });
  }
};