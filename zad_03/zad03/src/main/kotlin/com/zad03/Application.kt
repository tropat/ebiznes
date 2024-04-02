import discord4j.core.DiscordClientBuilder
import discord4j.common.util.Snowflake
import discord4j.core.`object`.entity.channel.MessageChannel

fun main() {
    val token = "MTIyNDQyNjY3Mzk3MDM1MjEyOA.GI0VVs.MqY7YbGn5-vFKn_kpL7eMtQrO3nW6RMem4rjEs"

    val client = DiscordClientBuilder.create(token).build()
    val gateway = client.login().block() ?: throw IllegalStateException("Nie udało się zalogować bota.")

    val channelId = Snowflake.of("1224428417563230253")

    val channel = gateway.getChannelById(channelId).ofType(MessageChannel::class.java).block()
        ?: throw IllegalStateException("Nie udało się znaleźć kanału Discord.")

    channel.createMessage("Witaj kanale").block()

    gateway.onDisconnect().block()
}
