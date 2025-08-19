from mcp.server.fastmcp import FastMCP
from zoneinfo import ZoneInfo
import datetime

# Crée un serveur MCP "haut niveau"
mcp = FastMCP("mcp-time")

@mcp.tool(
    name="now",
    description="Retourne l'heure actuelle en ISO et formatée pour un fuseau horaire donné."
)
def now(locale: str = "fr-FR", timeZone: str = "Europe/Paris") -> dict:
    """
    Args:
      locale: code de langue (pour compat, non utilisé par strftime)
      timeZone: identifiant IANA (ex: Europe/Paris, UTC, America/New_York)
    """
    tz = ZoneInfo(timeZone)
    dt = datetime.datetime.now(tz)
    return {
        "iso": dt.isoformat(),
        "formatted": dt.strftime("%c"),
        "epochMs": int(dt.timestamp() * 1000),
        "timeZone": str(dt.tzinfo),
    }

def main() -> None:
    # Lance le serveur en transport STDIO (parfait pour Watson Orchestrate)
    mcp.run(transport="stdio")

if __name__ == "__main__":
    main()
