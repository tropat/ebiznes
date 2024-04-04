import discord4j.core.DiscordClientBuilder
import discord4j.common.util.Snowflake
import discord4j.core.`object`.entity.channel.MessageChannel
import discord4j.core.event.domain.message.MessageCreateEvent

fun main() {
    val token = "MTIyNDQyNjY3Mzk3MDM1MjEyOA.GHKp2r.wDf347E93Q-BzknHQ6Nufih3E6bjMTpQPugHgA"

    val client = DiscordClientBuilder.create(token).build()
    val gateway = client.login().block() ?: throw IllegalStateException("Nie udało się zalogować bota.")

    val channelId = Snowflake.of("1224428417563230253")

    val channel = gateway.getChannelById(channelId).ofType(MessageChannel::class.java).block()
        ?: throw IllegalStateException("Nie udało się znaleźć kanału Discord.")

    channel.createMessage("Wpisz 'kategorie @test' aby poznac dostepne kategorie!").block()

    gateway.eventDispatcher.on(MessageCreateEvent::class.java)
        .filter { event ->
            val mentionedBot = event.message.userMentions.any { it.isBot && it.username == "test" }
            !event.message.author.get().isBot && mentionedBot
        }
        .subscribe { event ->
            val messageContent = event.message.content
            if(messageContent.split(" ")[0]=="kategorie") {
                channel.createMessage("Lista kategorii: koty, psy, konie. Wpisz 'nazwa_kategorii @test'").block()
            } else {
                when (messageContent.split(" ")[0]) {
                    "psy" -> {
                        channel.createMessage("Rasy psow: corgi, corgi, corgi").block()
                    }
                    "koty" -> {
                        channel.createMessage("Rasy kotow: dachowiec, dachowiec, dachowiec").block()
                    }
                    "konie" -> {
                        channel.createMessage("Rasy koni: kon, kon, kon").block()
                    }
                    else -> {
                        println("Nieznana kategoria")
                    }
                }
            }
        }

    gateway.onDisconnect().block()
}