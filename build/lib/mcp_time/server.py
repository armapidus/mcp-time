from mcp.server import Server
from mcp.transport.stdio import StdioServerTransport
from zoneinfo import ZoneInfo
import datetime
import asyncio

# Déclare le serveur MCP
server = Server(name="mcp-time", version="0.1.0")

# Outil: renvoie l'heure actuelle pour un fuseau donné
@server.tool(
    name="now",
    description="Retourne l'heure actuelle en ISO et formatée pour un fuseau horaire donné."
)
async def now(locale: str = "fr-FR", timeZone: str = "Europe/Paris") -> dict:
    """
    Args:
      locale: code de langue (non utilisé pour le formatage strftime, laissé pour compat)
      timeZone: identifiant IANA (ex: Europe/Paris, UTC, America/New_York)
    Returns:
      Dict JSON-sérialisable avec l'heure actuelle.
    """
    tz = ZoneInfo(timeZone)
    dt = datetime.datetime.now(tz)
    return {
        "iso": dt.isoformat(),
        "formatted": dt.strftime("%c"),
        "epochMs": int(dt.timestamp() * 1000),
        "timeZone": str(dt.tzinfo)
    }

# Boucle principale (transport STDIO pour Watson Orchestrate)
async def main() -> None:
    transport = StdioServerTransport()
    await server.run(transport)

if __name__ == "__main__":
    asyncio.run(main())
