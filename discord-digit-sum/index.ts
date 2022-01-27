import DiscordJS, { Intents, TextChannel } from "discord.js";
import dotenv from "dotenv";
dotenv.config();

const client = new DiscordJS.Client({
  intents: [Intents.FLAGS.GUILDS, Intents.FLAGS.GUILD_MESSAGES],
});

client.on("ready", () => {
  console.log("ready");
});

client.on("messageCreate", (message) => {
  //   console.log(message.content);
  const sum = message.content
    .split("")
    .reduce((acc, cur) => acc + parseInt(cur), 0);
  // post in the channel 935951820994535487
  //   client.channels.fetch("935951820994535487").then((channel) => {
  //     channel.send(sum);
  //   });
  const channel = client.channels.cache.find(
    (channel) => channel.id === "935951820994535487"
  );
  //   console.log(channel.);
  (channel as TextChannel).send(sum.toString());
});

client.login(process.env.TOKEN);
