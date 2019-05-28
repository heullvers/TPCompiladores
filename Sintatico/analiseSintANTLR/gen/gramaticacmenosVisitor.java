// Generated from /home/heuller/Documents/2019-1/Compiladores/analiseSintANTLR/src/gramaticacmenos.g4 by ANTLR 4.7.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link gramaticacmenosParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface gramaticacmenosVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#programa}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrograma(gramaticacmenosParser.ProgramaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#declaracao_lista}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao_lista(gramaticacmenosParser.Declaracao_listaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#declaracao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclaracao(gramaticacmenosParser.DeclaracaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#var_declaracao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar_declaracao(gramaticacmenosParser.Var_declaracaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#tipo_especificador}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTipo_especificador(gramaticacmenosParser.Tipo_especificadorContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#atributos_declaracao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtributos_declaracao(gramaticacmenosParser.Atributos_declaracaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#fun_declaracao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFun_declaracao(gramaticacmenosParser.Fun_declaracaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#params}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParams(gramaticacmenosParser.ParamsContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#param_lista}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam_lista(gramaticacmenosParser.Param_listaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#param}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParam(gramaticacmenosParser.ParamContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#composto_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComposto_decl(gramaticacmenosParser.Composto_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#local_declaracoes}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLocal_declaracoes(gramaticacmenosParser.Local_declaracoesContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#comando_lista}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComando_lista(gramaticacmenosParser.Comando_listaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#comando}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitComando(gramaticacmenosParser.ComandoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#expressao_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao_decl(gramaticacmenosParser.Expressao_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#selecao_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSelecao_decl(gramaticacmenosParser.Selecao_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#iteracao_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIteracao_decl(gramaticacmenosParser.Iteracao_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#retorno_decl}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRetorno_decl(gramaticacmenosParser.Retorno_declContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#expressao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao(gramaticacmenosParser.ExpressaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#var}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitVar(gramaticacmenosParser.VarContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#expressao_simples}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao_simples(gramaticacmenosParser.Expressao_simplesContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#relacional}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelacional(gramaticacmenosParser.RelacionalContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#expressao_soma}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressao_soma(gramaticacmenosParser.Expressao_somaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#soma}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitSoma(gramaticacmenosParser.SomaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#termo}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTermo(gramaticacmenosParser.TermoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#mult}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMult(gramaticacmenosParser.MultContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#fator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFator(gramaticacmenosParser.FatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#ativacao}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAtivacao(gramaticacmenosParser.AtivacaoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#args}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgs(gramaticacmenosParser.ArgsContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#arg_lista}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArg_lista(gramaticacmenosParser.Arg_listaContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#num}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNum(gramaticacmenosParser.NumContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#num_int}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitNum_int(gramaticacmenosParser.Num_intContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#digito}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDigito(gramaticacmenosParser.DigitoContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#ident}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIdent(gramaticacmenosParser.IdentContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#letra}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLetra(gramaticacmenosParser.LetraContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#abre_chave}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbre_chave(gramaticacmenosParser.Abre_chaveContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#fecha_chave}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFecha_chave(gramaticacmenosParser.Fecha_chaveContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#abre_colchete}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAbre_colchete(gramaticacmenosParser.Abre_colcheteContext ctx);
	/**
	 * Visit a parse tree produced by {@link gramaticacmenosParser#fecha_colchete}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFecha_colchete(gramaticacmenosParser.Fecha_colcheteContext ctx);
}