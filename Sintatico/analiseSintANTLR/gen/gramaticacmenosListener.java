// Generated from /home/heuller/Documents/2019-1/Compiladores/analiseSintANTLR/src/gramaticacmenos.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link gramaticacmenosParser}.
 */
public interface gramaticacmenosListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#programa}.
	 * @param ctx the parse tree
	 */
	void enterPrograma(gramaticacmenosParser.ProgramaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#programa}.
	 * @param ctx the parse tree
	 */
	void exitPrograma(gramaticacmenosParser.ProgramaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#declaracao_lista}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao_lista(gramaticacmenosParser.Declaracao_listaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#declaracao_lista}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao_lista(gramaticacmenosParser.Declaracao_listaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void enterDeclaracao(gramaticacmenosParser.DeclaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#declaracao}.
	 * @param ctx the parse tree
	 */
	void exitDeclaracao(gramaticacmenosParser.DeclaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#var_declaracao}.
	 * @param ctx the parse tree
	 */
	void enterVar_declaracao(gramaticacmenosParser.Var_declaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#var_declaracao}.
	 * @param ctx the parse tree
	 */
	void exitVar_declaracao(gramaticacmenosParser.Var_declaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#tipo_especificador}.
	 * @param ctx the parse tree
	 */
	void enterTipo_especificador(gramaticacmenosParser.Tipo_especificadorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#tipo_especificador}.
	 * @param ctx the parse tree
	 */
	void exitTipo_especificador(gramaticacmenosParser.Tipo_especificadorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#atributos_declaracao}.
	 * @param ctx the parse tree
	 */
	void enterAtributos_declaracao(gramaticacmenosParser.Atributos_declaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#atributos_declaracao}.
	 * @param ctx the parse tree
	 */
	void exitAtributos_declaracao(gramaticacmenosParser.Atributos_declaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#fun_declaracao}.
	 * @param ctx the parse tree
	 */
	void enterFun_declaracao(gramaticacmenosParser.Fun_declaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#fun_declaracao}.
	 * @param ctx the parse tree
	 */
	void exitFun_declaracao(gramaticacmenosParser.Fun_declaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#params}.
	 * @param ctx the parse tree
	 */
	void enterParams(gramaticacmenosParser.ParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#params}.
	 * @param ctx the parse tree
	 */
	void exitParams(gramaticacmenosParser.ParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#param_lista}.
	 * @param ctx the parse tree
	 */
	void enterParam_lista(gramaticacmenosParser.Param_listaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#param_lista}.
	 * @param ctx the parse tree
	 */
	void exitParam_lista(gramaticacmenosParser.Param_listaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(gramaticacmenosParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(gramaticacmenosParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#composto_decl}.
	 * @param ctx the parse tree
	 */
	void enterComposto_decl(gramaticacmenosParser.Composto_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#composto_decl}.
	 * @param ctx the parse tree
	 */
	void exitComposto_decl(gramaticacmenosParser.Composto_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#local_declaracoes}.
	 * @param ctx the parse tree
	 */
	void enterLocal_declaracoes(gramaticacmenosParser.Local_declaracoesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#local_declaracoes}.
	 * @param ctx the parse tree
	 */
	void exitLocal_declaracoes(gramaticacmenosParser.Local_declaracoesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#comando_lista}.
	 * @param ctx the parse tree
	 */
	void enterComando_lista(gramaticacmenosParser.Comando_listaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#comando_lista}.
	 * @param ctx the parse tree
	 */
	void exitComando_lista(gramaticacmenosParser.Comando_listaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#comando}.
	 * @param ctx the parse tree
	 */
	void enterComando(gramaticacmenosParser.ComandoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#comando}.
	 * @param ctx the parse tree
	 */
	void exitComando(gramaticacmenosParser.ComandoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#expressao_decl}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_decl(gramaticacmenosParser.Expressao_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#expressao_decl}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_decl(gramaticacmenosParser.Expressao_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#selecao_decl}.
	 * @param ctx the parse tree
	 */
	void enterSelecao_decl(gramaticacmenosParser.Selecao_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#selecao_decl}.
	 * @param ctx the parse tree
	 */
	void exitSelecao_decl(gramaticacmenosParser.Selecao_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#iteracao_decl}.
	 * @param ctx the parse tree
	 */
	void enterIteracao_decl(gramaticacmenosParser.Iteracao_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#iteracao_decl}.
	 * @param ctx the parse tree
	 */
	void exitIteracao_decl(gramaticacmenosParser.Iteracao_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#retorno_decl}.
	 * @param ctx the parse tree
	 */
	void enterRetorno_decl(gramaticacmenosParser.Retorno_declContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#retorno_decl}.
	 * @param ctx the parse tree
	 */
	void exitRetorno_decl(gramaticacmenosParser.Retorno_declContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(gramaticacmenosParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(gramaticacmenosParser.ExpressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#var}.
	 * @param ctx the parse tree
	 */
	void enterVar(gramaticacmenosParser.VarContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#var}.
	 * @param ctx the parse tree
	 */
	void exitVar(gramaticacmenosParser.VarContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#expressao_simples}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_simples(gramaticacmenosParser.Expressao_simplesContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#expressao_simples}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_simples(gramaticacmenosParser.Expressao_simplesContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#relacional}.
	 * @param ctx the parse tree
	 */
	void enterRelacional(gramaticacmenosParser.RelacionalContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#relacional}.
	 * @param ctx the parse tree
	 */
	void exitRelacional(gramaticacmenosParser.RelacionalContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#expressao_soma}.
	 * @param ctx the parse tree
	 */
	void enterExpressao_soma(gramaticacmenosParser.Expressao_somaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#expressao_soma}.
	 * @param ctx the parse tree
	 */
	void exitExpressao_soma(gramaticacmenosParser.Expressao_somaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#soma}.
	 * @param ctx the parse tree
	 */
	void enterSoma(gramaticacmenosParser.SomaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#soma}.
	 * @param ctx the parse tree
	 */
	void exitSoma(gramaticacmenosParser.SomaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#termo}.
	 * @param ctx the parse tree
	 */
	void enterTermo(gramaticacmenosParser.TermoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#termo}.
	 * @param ctx the parse tree
	 */
	void exitTermo(gramaticacmenosParser.TermoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#mult}.
	 * @param ctx the parse tree
	 */
	void enterMult(gramaticacmenosParser.MultContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#mult}.
	 * @param ctx the parse tree
	 */
	void exitMult(gramaticacmenosParser.MultContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#fator}.
	 * @param ctx the parse tree
	 */
	void enterFator(gramaticacmenosParser.FatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#fator}.
	 * @param ctx the parse tree
	 */
	void exitFator(gramaticacmenosParser.FatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#ativacao}.
	 * @param ctx the parse tree
	 */
	void enterAtivacao(gramaticacmenosParser.AtivacaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#ativacao}.
	 * @param ctx the parse tree
	 */
	void exitAtivacao(gramaticacmenosParser.AtivacaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#args}.
	 * @param ctx the parse tree
	 */
	void enterArgs(gramaticacmenosParser.ArgsContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#args}.
	 * @param ctx the parse tree
	 */
	void exitArgs(gramaticacmenosParser.ArgsContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#arg_lista}.
	 * @param ctx the parse tree
	 */
	void enterArg_lista(gramaticacmenosParser.Arg_listaContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#arg_lista}.
	 * @param ctx the parse tree
	 */
	void exitArg_lista(gramaticacmenosParser.Arg_listaContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#num}.
	 * @param ctx the parse tree
	 */
	void enterNum(gramaticacmenosParser.NumContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#num}.
	 * @param ctx the parse tree
	 */
	void exitNum(gramaticacmenosParser.NumContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#num_int}.
	 * @param ctx the parse tree
	 */
	void enterNum_int(gramaticacmenosParser.Num_intContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#num_int}.
	 * @param ctx the parse tree
	 */
	void exitNum_int(gramaticacmenosParser.Num_intContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#digito}.
	 * @param ctx the parse tree
	 */
	void enterDigito(gramaticacmenosParser.DigitoContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#digito}.
	 * @param ctx the parse tree
	 */
	void exitDigito(gramaticacmenosParser.DigitoContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#ident}.
	 * @param ctx the parse tree
	 */
	void enterIdent(gramaticacmenosParser.IdentContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#ident}.
	 * @param ctx the parse tree
	 */
	void exitIdent(gramaticacmenosParser.IdentContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#letra}.
	 * @param ctx the parse tree
	 */
	void enterLetra(gramaticacmenosParser.LetraContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#letra}.
	 * @param ctx the parse tree
	 */
	void exitLetra(gramaticacmenosParser.LetraContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#abre_chave}.
	 * @param ctx the parse tree
	 */
	void enterAbre_chave(gramaticacmenosParser.Abre_chaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#abre_chave}.
	 * @param ctx the parse tree
	 */
	void exitAbre_chave(gramaticacmenosParser.Abre_chaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#fecha_chave}.
	 * @param ctx the parse tree
	 */
	void enterFecha_chave(gramaticacmenosParser.Fecha_chaveContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#fecha_chave}.
	 * @param ctx the parse tree
	 */
	void exitFecha_chave(gramaticacmenosParser.Fecha_chaveContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#abre_colchete}.
	 * @param ctx the parse tree
	 */
	void enterAbre_colchete(gramaticacmenosParser.Abre_colcheteContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#abre_colchete}.
	 * @param ctx the parse tree
	 */
	void exitAbre_colchete(gramaticacmenosParser.Abre_colcheteContext ctx);
	/**
	 * Enter a parse tree produced by {@link gramaticacmenosParser#fecha_colchete}.
	 * @param ctx the parse tree
	 */
	void enterFecha_colchete(gramaticacmenosParser.Fecha_colcheteContext ctx);
	/**
	 * Exit a parse tree produced by {@link gramaticacmenosParser#fecha_colchete}.
	 * @param ctx the parse tree
	 */
	void exitFecha_colchete(gramaticacmenosParser.Fecha_colcheteContext ctx);
}